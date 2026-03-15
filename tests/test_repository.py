from contextlib import redirect_stdout
import io
import os
from pathlib import Path
import tempfile
import unittest

from philosopher_agent.cli import main
from philosopher_agent.repository import (
    CardReference,
    build_graph_data,
    build_context_pack,
    create_card,
    find_explicit_contradictions,
    load_cards,
    search_cards,
    upsert_card_reference,
    validate_cards,
)


CARD_A = """---
id: knw-alpha
title: Alpha
status: stable
visibility: public
complexity: 2
references:
  - id: knw-beta
    relation: prerequisite
tags:
  - concept
derived_from_private: false
---

Alpha references Beta.
"""


CARD_B = """---
id: knw-beta
title: Beta
status: draft
visibility: public
complexity: 1
references: []
tags:
  - concept
derived_from_private: false
---

Beta is a standalone card.
"""


CARD_C = """---
id: knw-gamma
title: Gamma critique
status: stable
visibility: public
complexity: 2
references:
  - id: knw-beta
    relation: contradict
tags:
  - critique
  - metrics
derived_from_private: false
---

Gamma argues against Beta.
"""


CARD_D = """---
id: knw-delta
title: Delta support
status: draft
visibility: public
complexity: 1
references:
  - id: knw-alpha
    relation: support
tags:
  - workflow
derived_from_private: false
---

Delta adds supporting context for Alpha.
"""


def write_fixture_cards(repo_root: Path) -> None:
    knowledge_dir = repo_root / "vault" / "public" / "knowledge"
    knowledge_dir.mkdir(parents=True)
    (knowledge_dir / "knw-alpha.md").write_text(CARD_A, encoding="utf-8")
    (knowledge_dir / "knw-beta.md").write_text(CARD_B, encoding="utf-8")
    (knowledge_dir / "knw-gamma.md").write_text(CARD_C, encoding="utf-8")
    (knowledge_dir / "knw-delta.md").write_text(CARD_D, encoding="utf-8")


class RepositoryTests(unittest.TestCase):
    def test_load_and_validate_cards(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            cards = load_cards(repo_root)

            self.assertEqual(4, len(cards))
            self.assertEqual([], validate_cards(cards))
            self.assertEqual("prerequisite", cards[0].references[0].relation)

    def test_build_graph_data(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            cards = load_cards(repo_root)
            graph_data = build_graph_data(repo_root, cards)

            self.assertEqual("public", graph_data["mode"])
            self.assertEqual(4, graph_data["summary"]["cards"])
            self.assertEqual(3, graph_data["summary"]["edges"])

    def test_create_private_card(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            path = create_card(
                repo_root=repo_root,
                title="Local note",
                visibility="private",
                private_user="alice",
                references=[CardReference(target_id="knw-alpha", relation="related")],
            )

            self.assertTrue(path.exists())
            self.assertIn("vault/private/users/alice/knowledge", str(path))

    def test_search_cards(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            cards = load_cards(repo_root)
            matches = search_cards(cards, "critique metrics", limit=5)

            self.assertEqual("knw-gamma", matches[0]["card"].id)
            self.assertGreater(matches[0]["score"], 0)

    def test_build_context_pack(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            cards = load_cards(repo_root)
            pack = build_context_pack(
                repo_root=repo_root,
                cards=cards,
                seed_ids=["knw-beta"],
                depth=1,
                max_cards=3,
                body_chars=60,
            )

            selected_ids = [card["id"] for card in pack["cards"]]
            self.assertEqual("knw-beta", selected_ids[0])
            self.assertIn("knw-alpha", selected_ids)
            self.assertIn("knw-gamma", selected_ids)
            self.assertEqual(3, pack["summary"]["cards"])

    def test_find_explicit_contradictions(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            cards = load_cards(repo_root)
            result = find_explicit_contradictions(
                repo_root=repo_root,
                cards=cards,
                seed_ids=["knw-beta"],
                depth=1,
                max_cards=4,
            )

            self.assertEqual(1, result["summary"]["explicit_contradictions"])
            self.assertEqual("knw-gamma", result["contradictions"][0]["source_id"])
            self.assertEqual("knw-beta", result["contradictions"][0]["target_id"])

    def test_upsert_card_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            path, action = upsert_card_reference(
                repo_root=repo_root,
                source_id="knw-beta",
                target_id="knw-alpha",
                relation="support",
            )
            self.assertEqual("added", action)
            self.assertTrue(path.exists())

            cards = load_cards(repo_root)
            beta = {card.id: card for card in cards}["knw-beta"]
            self.assertEqual("knw-alpha", beta.references[0].target_id)
            self.assertEqual("support", beta.references[0].relation)

    def test_cli_context_pack(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            output = io.StringIO()
            cwd = Path.cwd()
            try:
                os.chdir(repo_root)
                with redirect_stdout(output):
                    exit_code = main(["context-pack", "knw-beta", "--depth", "1", "--max-cards", "3"])
            finally:
                os.chdir(cwd)

            self.assertEqual(0, exit_code)
            rendered = output.getvalue()
            self.assertIn("Context pack:", rendered)
            self.assertIn("knw-beta", rendered)
            self.assertIn("knw-gamma", rendered)

    def test_cli_find_contradictions_requires_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            repo_root = Path(tempdir)
            (repo_root / ".git").mkdir()
            write_fixture_cards(repo_root)

            output = io.StringIO()
            cwd = Path.cwd()
            try:
                os.chdir(repo_root)
                with redirect_stdout(output):
                    exit_code = main(["find-contradictions"])
            finally:
                os.chdir(cwd)

            self.assertEqual(1, exit_code)
            self.assertIn("Provide seed IDs or pass --all", output.getvalue())


if __name__ == "__main__":
    unittest.main()
