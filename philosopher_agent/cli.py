from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Optional

from .repository import (
    CardReference,
    RepositoryError,
    build_graph_data,
    build_context_pack,
    create_card,
    ensure_repository_layout,
    find_repo_root,
    find_explicit_contradictions,
    load_cards,
    search_cards,
    upsert_card_reference,
    validate_cards,
    write_graph,
)


def parse_reference_argument(raw_reference: str) -> CardReference:
    """Parse a CLI reference argument in the form id or id:relation."""

    raw_reference = raw_reference.strip()
    if not raw_reference:
        raise RepositoryError("Reference arguments cannot be empty.")

    parts = raw_reference.split(":", 1)
    if len(parts) == 1:
        return CardReference(target_id=parts[0])

    target_id, relation = parts[0].strip(), parts[1].strip()
    if not target_id or not relation:
        raise RepositoryError("Reference arguments must look like id or id:relation.")
    return CardReference(target_id=target_id, relation=relation)


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI parser."""

    parser = argparse.ArgumentParser(description="Manage Markdown knowledge cards.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Create a new knowledge card.")
    new_parser.add_argument("title", help="Card title.")
    new_parser.add_argument("--id", dest="card_id", help="Explicit knowledge card ID.")
    new_parser.add_argument(
        "--visibility",
        choices=["public", "private"],
        default="public",
        help="Card visibility scope.",
    )
    new_parser.add_argument("--user", help="Private user name for local cards.")
    new_parser.add_argument(
        "--status",
        choices=["draft", "stable"],
        default="draft",
        help="Initial card status.",
    )
    new_parser.add_argument(
        "--complexity",
        type=int,
        default=1,
        help="Complexity score from 1 to 5.",
    )
    new_parser.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Repeatable metadata tag.",
    )
    new_parser.add_argument(
        "--ref",
        action="append",
        default=[],
        help="Reference in the form id or id:relation.",
    )
    new_parser.add_argument(
        "--derived-from-private",
        action="store_true",
        help="Mark a public card as influenced by local private material.",
    )

    check_parser = subparsers.add_parser("check", help="Validate card metadata and references.")
    check_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user in validation.",
    )

    graph_parser = subparsers.add_parser("build-graph", help="Build the knowledge graph JSON.")
    graph_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user in the graph snapshot.",
    )

    link_parser = subparsers.add_parser("link", help="Add or update a reference between cards.")
    link_parser.add_argument("source_id", help="Source card ID.")
    link_parser.add_argument("target_id", help="Target card ID.")
    link_parser.add_argument(
        "--relation",
        default="related",
        help="Reference relation type. Defaults to 'related'.",
    )
    link_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user when resolving IDs.",
    )

    search_parser = subparsers.add_parser("search-cards", help="Search cards with bounded output.")
    search_parser.add_argument("query", help="Search query.")
    search_parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of matching cards to print.",
    )
    search_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user when searching.",
    )

    context_parser = subparsers.add_parser(
        "context-pack",
        help="Build a bounded local context pack around one or more seed cards.",
    )
    context_parser.add_argument("card_ids", nargs="+", help="Seed card IDs.")
    context_parser.add_argument(
        "--depth",
        type=int,
        default=1,
        help="Graph traversal depth from the seed cards.",
    )
    context_parser.add_argument(
        "--max-cards",
        type=int,
        default=8,
        help="Maximum number of cards to include in the pack.",
    )
    context_parser.add_argument(
        "--body-chars",
        type=int,
        default=280,
        help="Maximum number of body characters to print per card preview.",
    )
    context_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user when building the pack.",
    )

    contradictions_parser = subparsers.add_parser(
        "find-contradictions",
        help="Find explicit 'contradict' references in a bounded local graph.",
    )
    contradictions_parser.add_argument("card_ids", nargs="*", help="Optional seed card IDs.")
    contradictions_parser.add_argument(
        "--depth",
        type=int,
        default=1,
        help="Graph traversal depth from the seed cards.",
    )
    contradictions_parser.add_argument(
        "--max-cards",
        type=int,
        default=8,
        help="Maximum number of cards to scan when seeds are provided.",
    )
    contradictions_parser.add_argument(
        "--body-chars",
        type=int,
        default=200,
        help="Maximum preview size for the optional embedded context pack.",
    )
    contradictions_parser.add_argument(
        "--all",
        action="store_true",
        help="Scan the full loaded scope instead of requiring seed IDs.",
    )
    contradictions_parser.add_argument(
        "--private-user",
        help="Include local private cards for the given user when scanning.",
    )

    return parser


def render_context_pack(pack: dict) -> None:
    print(
        "Context pack: %s card(s), %s edge(s), seeds=%s, depth=%s, max-cards=%s"
        % (
            pack["summary"]["cards"],
            pack["summary"]["edges"],
            ", ".join(pack["seed_ids"]),
            pack["depth"],
            pack["max_cards"],
        )
    )
    for card in pack["cards"]:
        print(
            "- [%s] %s | %s | %s"
            % (card["distance"], card["id"], card["status"], card["title"])
        )
        print("  path: %s" % card["path"])
        if card["tags"]:
            print("  tags: %s" % ", ".join(card["tags"]))
        if card["body_preview"]:
            print("  body: %s" % card["body_preview"])

    if not pack["edges"]:
        print("Edges: none")
        return

    print("Edges:")
    for edge in pack["edges"]:
        print("- %s -[%s]-> %s" % (edge["source"], edge["relation"], edge["target"]))


def command_new(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    references = [parse_reference_argument(item) for item in args.ref]
    created_path = create_card(
        repo_root=repo_root,
        title=args.title,
        visibility=args.visibility,
        private_user=args.user,
        status=args.status,
        complexity=args.complexity,
        card_id=args.card_id,
        tags=args.tag,
        references=references,
        derived_from_private=args.derived_from_private,
    )
    print("Created %s" % created_path.relative_to(repo_root))
    return 0


def command_check(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    cards = load_cards(repo_root, args.private_user)
    issues = validate_cards(cards)
    if issues:
        for issue in issues:
            print("ERROR: %s" % issue)
        return 1

    scope = "public"
    if args.private_user:
        scope = "public + private:%s" % args.private_user
    print("Validation passed for %s cards in %s scope." % (len(cards), scope))
    return 0


def command_build_graph(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    cards = load_cards(repo_root, args.private_user)
    issues = validate_cards(cards)
    if issues:
        for issue in issues:
            print("ERROR: %s" % issue)
        return 1

    graph_data = build_graph_data(repo_root, cards, args.private_user)
    output_path = write_graph(repo_root, graph_data, args.private_user)
    print("Wrote %s" % output_path.relative_to(repo_root))
    return 0


def command_link(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    path, action = upsert_card_reference(
        repo_root=repo_root,
        source_id=args.source_id,
        target_id=args.target_id,
        relation=args.relation,
        private_user=args.private_user,
    )
    print("%s reference in %s" % (action.capitalize(), path.relative_to(repo_root)))
    return 0


def command_search_cards(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    cards = load_cards(repo_root, args.private_user)
    matches = search_cards(cards, args.query, args.limit)
    if not matches:
        print("No cards matched query '%s'." % args.query)
        return 0

    print("Found %s matching card(s)." % len(matches))
    for match in matches:
        card = match["card"]
        print(
            "- score=%s | %s | %s | %s"
            % (match["score"], card.id, card.status, card.title)
        )
        print("  path: %s" % card.path.relative_to(repo_root))
        if card.tags:
            print("  tags: %s" % ", ".join(card.tags))
    return 0


def command_context_pack(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    cards = load_cards(repo_root, args.private_user)
    pack = build_context_pack(
        repo_root=repo_root,
        cards=cards,
        seed_ids=args.card_ids,
        depth=args.depth,
        max_cards=args.max_cards,
        body_chars=args.body_chars,
    )
    render_context_pack(pack)
    return 0


def command_find_contradictions(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    ensure_repository_layout(repo_root)
    if not args.all and not args.card_ids:
        raise RepositoryError("Provide seed IDs or pass --all to scan the full loaded scope.")

    cards = load_cards(repo_root, args.private_user)
    result = find_explicit_contradictions(
        repo_root=repo_root,
        cards=cards,
        seed_ids=None if args.all else args.card_ids,
        depth=args.depth,
        max_cards=args.max_cards,
        body_chars=args.body_chars,
    )

    if result["context_pack"] is not None:
        render_context_pack(result["context_pack"])

    if not result["contradictions"]:
        print(
            "No explicit contradictions found in %s scope."
            % ("full" if args.all else "selected")
        )
        return 0

    print("Explicit contradictions: %s" % result["summary"]["explicit_contradictions"])
    for contradiction in result["contradictions"]:
        print(
            "- %s contradicts %s"
            % (contradiction["source_id"], contradiction["target_id"])
        )
        print("  source: %s" % contradiction["source_title"])
        print("  target: %s" % contradiction["target_title"])
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "new":
            return command_new(args)
        if args.command == "check":
            return command_check(args)
        if args.command == "build-graph":
            return command_build_graph(args)
        if args.command == "link":
            return command_link(args)
        if args.command == "search-cards":
            return command_search_cards(args)
        if args.command == "context-pack":
            return command_context_pack(args)
        if args.command == "find-contradictions":
            return command_find_contradictions(args)
    except RepositoryError as error:
        print("ERROR: %s" % error)
        return 1

    parser.print_help()
    return 1
