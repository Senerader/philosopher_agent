from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import getpass
import json
import os
import re
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import yaml


VALID_STATUS = {"draft", "stable"}
VALID_VISIBILITY = {"public", "private"}
RELATION_SORT_ORDER = {
    "prerequisite": 0,
    "support": 1,
    "contradict": 2,
    "example": 3,
    "related": 4,
}


class RepositoryError(Exception):
    """Raised when the repository state is invalid."""


@dataclass(frozen=True)
class CardReference:
    target_id: str
    relation: str = "related"


@dataclass
class KnowledgeCard:
    id: str
    title: str
    status: str
    visibility: str
    complexity: int
    references: List[CardReference] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    derived_from_private: bool = False
    body: str = ""
    path: Path = Path()


def find_repo_root(start: Optional[Path] = None) -> Path:
    """Find the repository root by walking upwards until .git is found."""

    current = (start or Path.cwd()).resolve()
    for candidate in [current] + list(current.parents):
        if (candidate / ".git").exists():
            return candidate
    raise RepositoryError("Could not find repository root. Run inside the git repo.")


def default_private_user() -> str:
    """Resolve the current local private user."""

    return os.environ.get("USER") or getpass.getuser()


def card_directory(repo_root: Path, visibility: str, private_user: Optional[str] = None) -> Path:
    """Return the directory where cards of the requested scope are stored."""

    if visibility not in VALID_VISIBILITY:
        raise RepositoryError("Visibility must be 'public' or 'private'.")

    if visibility == "public":
        return repo_root / "vault" / "public" / "knowledge"

    user = private_user or default_private_user()
    return repo_root / "vault" / "private" / "users" / user / "knowledge"


def assets_directory(repo_root: Path, visibility: str, private_user: Optional[str] = None) -> Path:
    """Return the directory where assets of the requested scope are stored."""

    if visibility == "public":
        return repo_root / "vault" / "public" / "assets"

    user = private_user or default_private_user()
    return repo_root / "vault" / "private" / "users" / user / "assets"


def ensure_repository_layout(repo_root: Path) -> None:
    """Create the minimal directory layout expected by the CLI."""

    required_dirs = [
        repo_root / "vault" / "public" / "knowledge",
        repo_root / "vault" / "public" / "assets",
        repo_root / "vault" / "private",
        repo_root / "vault" / "private" / "users",
        repo_root / "staging" / "imports",
        repo_root / "staging" / "chunks",
        repo_root / "index" / "graph",
        repo_root / "exports",
    ]

    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)


def parse_reference(raw_reference: object) -> CardReference:
    """Normalize a raw YAML reference entry."""

    if isinstance(raw_reference, str):
        target_id = raw_reference.strip()
        if not target_id:
            raise RepositoryError("Reference IDs cannot be empty.")
        return CardReference(target_id=target_id)

    if isinstance(raw_reference, dict):
        target_id = str(raw_reference.get("id", "")).strip()
        relation = str(raw_reference.get("relation", "related")).strip() or "related"
        if not target_id:
            raise RepositoryError("Reference objects must define a non-empty 'id'.")
        return CardReference(target_id=target_id, relation=relation)

    raise RepositoryError("References must be strings or objects with 'id' and optional 'relation'.")


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    """Split a Markdown file into YAML frontmatter and body."""

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise RepositoryError("Knowledge cards must start with YAML frontmatter.")

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :]).lstrip("\n")
            metadata = yaml.safe_load(frontmatter) or {}
            if not isinstance(metadata, dict):
                raise RepositoryError("YAML frontmatter must define an object.")
            return metadata, body

    raise RepositoryError("Knowledge card frontmatter is not closed.")


def load_card(path: Path) -> KnowledgeCard:
    """Load a single knowledge card from disk."""

    metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))

    try:
        complexity = int(metadata.get("complexity", 1))
    except (TypeError, ValueError):
        raise RepositoryError("Card complexity must be an integer.")

    raw_references = metadata.get("references", [])
    if raw_references is None:
        raw_references = []
    if not isinstance(raw_references, list):
        raise RepositoryError("Card references must be a list.")

    raw_tags = metadata.get("tags", [])
    if raw_tags is None:
        raw_tags = []
    if not isinstance(raw_tags, list):
        raise RepositoryError("Card tags must be a list.")

    return KnowledgeCard(
        id=str(metadata.get("id", "")).strip(),
        title=str(metadata.get("title", "")).strip(),
        status=str(metadata.get("status", "draft")).strip(),
        visibility=str(metadata.get("visibility", "public")).strip(),
        complexity=complexity,
        references=[parse_reference(item) for item in raw_references],
        tags=[str(tag).strip() for tag in raw_tags if str(tag).strip()],
        derived_from_private=bool(metadata.get("derived_from_private", False)),
        body=body,
        path=path,
    )


def iter_card_paths(repo_root: Path, private_user: Optional[str] = None) -> Iterable[Path]:
    """Yield public and optional private card paths."""

    public_dir = card_directory(repo_root, "public")
    if public_dir.exists():
        for path in sorted(public_dir.glob("*.md")):
            yield path

    if private_user:
        private_dir = card_directory(repo_root, "private", private_user)
        if private_dir.exists():
            for path in sorted(private_dir.glob("*.md")):
                yield path


def load_cards(repo_root: Path, private_user: Optional[str] = None) -> List[KnowledgeCard]:
    """Load all cards in scope."""

    cards = []
    for path in iter_card_paths(repo_root, private_user):
        cards.append(load_card(path))
    return cards


def card_index(cards: Sequence[KnowledgeCard]) -> Dict[str, KnowledgeCard]:
    """Index cards by their knowledge-card ID."""

    return {card.id: card for card in cards}


def serialize_reference(reference: CardReference) -> object:
    """Render a reference in the repository YAML format."""

    if reference.relation == "related":
        return reference.target_id
    return {"id": reference.target_id, "relation": reference.relation}


def normalize_preview(text: str, limit: int) -> str:
    """Collapse whitespace and shorten long bodies for compact output."""

    normalized = re.sub(r"\s+", " ", text).strip()
    if limit < 0:
        raise RepositoryError("Preview limits must be zero or greater.")
    if limit == 0 or len(normalized) <= limit:
        return normalized
    if limit <= 3:
        return normalized[:limit]
    return normalized[: limit - 3].rstrip() + "..."


def build_connection_maps(
    cards: Sequence[KnowledgeCard],
) -> Tuple[Dict[str, List[Dict[str, str]]], Dict[str, List[Dict[str, str]]]]:
    """Build outgoing and incoming edge maps for loaded cards."""

    outgoing = {card.id: [] for card in cards}
    incoming = {card.id: [] for card in cards}
    for card in cards:
        for reference in card.references:
            edge = {
                "source": card.id,
                "target": reference.target_id,
                "relation": reference.relation,
            }
            outgoing[card.id].append(edge)
            if reference.target_id in incoming:
                incoming[reference.target_id].append(edge)
    return outgoing, incoming


def search_cards(cards: Sequence[KnowledgeCard], query: str, limit: int = 10) -> List[Dict[str, object]]:
    """Search cards by ID, title, tags, and body with simple scoring."""

    raw_terms = [term.lower() for term in query.split() if term.strip()]
    if not raw_terms:
        raise RepositoryError("Search query cannot be empty.")
    if limit < 1:
        raise RepositoryError("Search limit must be at least 1.")

    results: List[Dict[str, object]] = []
    for card in cards:
        score = 0
        title = card.title.lower()
        card_id = card.id.lower()
        tags = [tag.lower() for tag in card.tags]
        body = card.body.lower()

        for term in raw_terms:
            if term in card_id:
                score += 6
            if term in title:
                score += 5
            if any(term in tag for tag in tags):
                score += 3
            if term in body:
                score += 1

        if score == 0:
            continue

        results.append(
            {
                "score": score,
                "card": card,
            }
        )

    results.sort(
        key=lambda item: (
            -int(item["score"]),
            0 if item["card"].status == "stable" else 1,
            item["card"].title.lower(),
            item["card"].id,
        )
    )
    return results[:limit]


def build_context_pack(
    repo_root: Path,
    cards: Sequence[KnowledgeCard],
    seed_ids: Sequence[str],
    depth: int = 1,
    max_cards: int = 8,
    body_chars: int = 280,
) -> Dict[str, object]:
    """Build a bounded local subgraph around one or more seed cards."""

    if depth < 0:
        raise RepositoryError("Context-pack depth must be zero or greater.")
    if max_cards < 1:
        raise RepositoryError("Context-pack max-cards must be at least 1.")

    deduped_seed_ids = []
    for seed_id in seed_ids:
        normalized = seed_id.strip()
        if normalized and normalized not in deduped_seed_ids:
            deduped_seed_ids.append(normalized)
    if not deduped_seed_ids:
        raise RepositoryError("Context-pack requires at least one seed ID.")
    if len(deduped_seed_ids) > max_cards:
        raise RepositoryError("Context-pack max-cards must be at least the number of seed IDs.")

    cards_by_id = card_index(cards)
    missing_seed_ids = [seed_id for seed_id in deduped_seed_ids if seed_id not in cards_by_id]
    if missing_seed_ids:
        raise RepositoryError("Unknown card ID(s): %s" % ", ".join(missing_seed_ids))

    outgoing, incoming = build_connection_maps(cards)

    def ranked_neighbors(card_id: str) -> List[str]:
        candidates = []
        for edge in outgoing.get(card_id, []):
            target_card = cards_by_id.get(edge["target"])
            if target_card is None:
                continue
            candidates.append(
                (
                    RELATION_SORT_ORDER.get(edge["relation"], 99),
                    0,
                    0 if target_card.status == "stable" else 1,
                    target_card.title.lower(),
                    target_card.id,
                )
            )
        for edge in incoming.get(card_id, []):
            source_card = cards_by_id.get(edge["source"])
            if source_card is None:
                continue
            candidates.append(
                (
                    RELATION_SORT_ORDER.get(edge["relation"], 99),
                    1,
                    0 if source_card.status == "stable" else 1,
                    source_card.title.lower(),
                    source_card.id,
                )
            )
        candidates.sort()
        return [candidate[-1] for candidate in candidates]

    selected_ids: List[str] = []
    distances: Dict[str, int] = {}
    queue = deque((seed_id, 0) for seed_id in deduped_seed_ids)
    enqueued = set(deduped_seed_ids)

    while queue and len(selected_ids) < max_cards:
        current_id, current_depth = queue.popleft()
        if current_id in distances:
            continue

        distances[current_id] = current_depth
        selected_ids.append(current_id)

        if current_depth >= depth:
            continue

        for neighbor_id in ranked_neighbors(current_id):
            if neighbor_id in distances or neighbor_id in enqueued:
                continue
            queue.append((neighbor_id, current_depth + 1))
            enqueued.add(neighbor_id)

    selected_set = set(selected_ids)
    selected_edges = [
        {
            "source": card.id,
            "target": reference.target_id,
            "relation": reference.relation,
        }
        for card in cards
        for reference in card.references
        if card.id in selected_set and reference.target_id in selected_set
    ]

    return {
        "seed_ids": deduped_seed_ids,
        "depth": depth,
        "max_cards": max_cards,
        "summary": {
            "cards": len(selected_ids),
            "edges": len(selected_edges),
        },
        "cards": [
            {
                "id": card_id,
                "title": cards_by_id[card_id].title,
                "status": cards_by_id[card_id].status,
                "visibility": cards_by_id[card_id].visibility,
                "complexity": cards_by_id[card_id].complexity,
                "tags": cards_by_id[card_id].tags,
                "distance": distances[card_id],
                "path": str(cards_by_id[card_id].path.relative_to(repo_root)),
                "body_preview": normalize_preview(cards_by_id[card_id].body, body_chars),
            }
            for card_id in selected_ids
        ],
        "edges": selected_edges,
    }


def find_explicit_contradictions(
    repo_root: Path,
    cards: Sequence[KnowledgeCard],
    seed_ids: Optional[Sequence[str]] = None,
    depth: int = 1,
    max_cards: int = 8,
    body_chars: int = 200,
) -> Dict[str, object]:
    """Find explicit contradiction edges in either a bounded pack or full scope."""

    if seed_ids:
        context_pack = build_context_pack(
            repo_root=repo_root,
            cards=cards,
            seed_ids=seed_ids,
            depth=depth,
            max_cards=max_cards,
            body_chars=body_chars,
        )
        selected_ids = {card["id"] for card in context_pack["cards"]}
    else:
        context_pack = None
        selected_ids = {card.id for card in cards}

    cards_by_id = card_index(cards)
    contradictions = []
    for card in cards:
        if card.id not in selected_ids:
            continue
        for reference in card.references:
            if reference.relation != "contradict":
                continue
            if reference.target_id not in selected_ids:
                continue
            target_card = cards_by_id.get(reference.target_id)
            if target_card is None:
                continue
            contradictions.append(
                {
                    "source_id": card.id,
                    "source_title": card.title,
                    "target_id": target_card.id,
                    "target_title": target_card.title,
                    "source_path": str(card.path.relative_to(repo_root)),
                    "target_path": str(target_card.path.relative_to(repo_root)),
                }
            )

    contradictions.sort(key=lambda item: (item["source_title"].lower(), item["target_title"].lower()))
    return {
        "scope": "context-pack" if seed_ids else "all-cards",
        "seed_ids": list(seed_ids or []),
        "summary": {
            "selected_cards": len(selected_ids),
            "explicit_contradictions": len(contradictions),
        },
        "context_pack": context_pack,
        "contradictions": contradictions,
    }


def upsert_card_reference(
    repo_root: Path,
    source_id: str,
    target_id: str,
    relation: str = "related",
    private_user: Optional[str] = None,
) -> Tuple[Path, str]:
    """Add or update a reference on an existing card."""

    source_id = source_id.strip()
    target_id = target_id.strip()
    relation = relation.strip() or "related"
    if not source_id or not target_id:
        raise RepositoryError("Source and target IDs are required.")

    cards = load_cards(repo_root, private_user)
    cards_by_id = card_index(cards)
    source_card = cards_by_id.get(source_id)
    if source_card is None:
        raise RepositoryError("Unknown source card ID '%s'." % source_id)
    if target_id not in cards_by_id:
        raise RepositoryError("Unknown target card ID '%s'." % target_id)

    metadata, body = parse_frontmatter(source_card.path.read_text(encoding="utf-8"))
    raw_references = metadata.get("references", [])
    if raw_references is None:
        raw_references = []
    references = [parse_reference(item) for item in raw_references]

    action = "added"
    for index, reference in enumerate(references):
        if reference.target_id != target_id:
            continue
        if reference.relation == relation:
            action = "unchanged"
        else:
            references[index] = CardReference(target_id=target_id, relation=relation)
            action = "updated"
        break
    else:
        references.append(CardReference(target_id=target_id, relation=relation))

    metadata["references"] = [serialize_reference(reference) for reference in references]
    frontmatter = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=False).strip()
    content = "---\n%s\n---\n\n%s" % (frontmatter, body)
    source_card.path.write_text(content, encoding="utf-8")
    return source_card.path, action


def validate_cards(cards: Sequence[KnowledgeCard]) -> List[str]:
    """Validate a set of loaded knowledge cards."""

    issues: List[str] = []
    seen_ids: Dict[str, Path] = {}

    for card in cards:
        if not card.id:
            issues.append("%s: missing id" % card.path)
        elif card.id in seen_ids:
            issues.append(
                "%s: duplicate id '%s' already used by %s" % (card.path, card.id, seen_ids[card.id])
            )
        else:
            seen_ids[card.id] = card.path

        if not card.title:
            issues.append("%s: missing title" % card.path)
        if card.status not in VALID_STATUS:
            issues.append("%s: invalid status '%s'" % (card.path, card.status))
        if card.visibility not in VALID_VISIBILITY:
            issues.append("%s: invalid visibility '%s'" % (card.path, card.visibility))
        if "vault/public/knowledge" in str(card.path).replace("\\", "/") and card.visibility != "public":
            issues.append("%s: card is stored in public knowledge but visibility is not public" % card.path)
        if "vault/private/users/" in str(card.path).replace("\\", "/") and card.visibility != "private":
            issues.append("%s: card is stored in private knowledge but visibility is not private" % card.path)
        if card.complexity < 1 or card.complexity > 5:
            issues.append("%s: complexity must be between 1 and 5" % card.path)
        if not card.body.strip():
            issues.append("%s: card body is empty" % card.path)

        local_targets = set()
        for reference in card.references:
            if reference.target_id == card.id:
                issues.append("%s: self-reference '%s' is not allowed" % (card.path, card.id))
            if reference.target_id in local_targets:
                issues.append("%s: duplicate reference to '%s'" % (card.path, reference.target_id))
            local_targets.add(reference.target_id)

    known_ids = {card.id for card in cards}
    for card in cards:
        for reference in card.references:
            if reference.target_id not in known_ids:
                issues.append(
                    "%s: reference '%s' does not match any loaded card" % (card.path, reference.target_id)
                )

    return issues


def build_graph_data(repo_root: Path, cards: Sequence[KnowledgeCard], private_user: Optional[str] = None) -> Dict[str, object]:
    """Build a graph representation for loaded cards."""

    mode = "public"
    if private_user:
        mode = "public+private:%s" % private_user

    edges = [
        {
            "source": card.id,
            "target": reference.target_id,
            "relation": reference.relation,
        }
        for card in cards
        for reference in card.references
    ]

    adjacency = {card.id: [] for card in cards}
    backlinks = {card.id: [] for card in cards}
    for edge in edges:
        adjacency[edge["source"]].append(
            {"target": edge["target"], "relation": edge["relation"]}
        )
        if edge["target"] in backlinks:
            backlinks[edge["target"]].append(
                {"source": edge["source"], "relation": edge["relation"]}
            )

    return {
        "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "mode": mode,
        "summary": {
            "cards": len(cards),
            "edges": len(edges),
            "stable_cards": sum(1 for card in cards if card.status == "stable"),
        },
        "cards": [
            {
                "id": card.id,
                "title": card.title,
                "status": card.status,
                "visibility": card.visibility,
                "complexity": card.complexity,
                "tags": card.tags,
                "derived_from_private": card.derived_from_private,
                "path": str(card.path.relative_to(repo_root)),
            }
            for card in cards
        ],
        "edges": edges,
        "adjacency": adjacency,
        "backlinks": backlinks,
    }


def graph_output_path(repo_root: Path, private_user: Optional[str] = None) -> Path:
    """Return the output path for a graph snapshot."""

    name = "public.json"
    if private_user:
        name = "%s.json" % private_user
    return repo_root / "index" / "graph" / name


def write_graph(repo_root: Path, graph_data: Dict[str, object], private_user: Optional[str] = None) -> Path:
    """Persist a generated graph snapshot as JSON."""

    output_path = graph_output_path(repo_root, private_user)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph_data, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return output_path


def create_card(
    repo_root: Path,
    title: str,
    visibility: str = "public",
    private_user: Optional[str] = None,
    status: str = "draft",
    complexity: int = 1,
    card_id: Optional[str] = None,
    tags: Optional[Sequence[str]] = None,
    references: Optional[Sequence[CardReference]] = None,
    derived_from_private: bool = False,
) -> Path:
    """Create a new knowledge card from a simple template."""

    ensure_repository_layout(repo_root)

    if status not in VALID_STATUS:
        raise RepositoryError("Status must be 'draft' or 'stable'.")
    if visibility not in VALID_VISIBILITY:
        raise RepositoryError("Visibility must be 'public' or 'private'.")
    if complexity < 1 or complexity > 5:
        raise RepositoryError("Complexity must be between 1 and 5.")

    if not title.strip():
        raise RepositoryError("Title cannot be empty.")

    resolved_id = card_id or ("knw-" + datetime.utcnow().strftime("%Y%m%d-%H%M%S"))
    destination_dir = card_directory(repo_root, visibility, private_user)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_path = destination_dir / ("%s.md" % resolved_id)

    if destination_path.exists():
        raise RepositoryError("Card already exists: %s" % destination_path)

    payload = {
        "id": resolved_id,
        "title": title.strip(),
        "status": status,
        "visibility": visibility,
        "complexity": complexity,
        "references": [
            (
                reference.target_id
                if reference.relation == "related"
                else {"id": reference.target_id, "relation": reference.relation}
            )
            for reference in (references or [])
        ],
        "tags": list(tags or []),
        "derived_from_private": derived_from_private,
    }

    frontmatter = yaml.safe_dump(payload, sort_keys=False, allow_unicode=False).strip()
    body = "# Material\n\nDescribe the knowledge here.\n"
    content = "---\n%s\n---\n\n%s" % (frontmatter, body)
    destination_path.write_text(content, encoding="utf-8")
    return destination_path
