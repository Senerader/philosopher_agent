# Philosopher Agent Instructions

This repository is a file-first knowledge graph for Markdown knowledge cards.

## Primary goal

Help the user create, connect, validate, and evolve knowledge cards.

A knowledge card is the only primary entity in the repository.

Each card must contain:

1. Material in the Markdown body
2. References to other knowledge cards in YAML frontmatter

There is no separate synthesis entity. A synthesis is just another knowledge
card with references to older cards.

## Repository layout

```text
vault/
  public/
    knowledge/
    assets/
  private/
    users/
      <username>/
        knowledge/
        assets/
staging/
  imports/
  chunks/
index/
  graph/
exports/
philosopher_agent/
```

## Knowledge card contract

Every card is a `.md` file with YAML frontmatter:

```yaml
id: knw-...
title: ...
status: draft | stable
visibility: public | private
complexity: 1..5
references:
  - knw-other-card
  - id: knw-another-card
    relation: prerequisite
tags: [...]
derived_from_private: false
```

Rules:

- Keep the actual knowledge in the Markdown body.
- Use `references` for graph edges.
- Prefer explicit typed relations when useful: `related`, `prerequisite`,
  `support`, `contradict`, `example`.
- If a public card depends on local private material, do not reference private
  IDs from the public card. Set `derived_from_private: true` instead.
- `stable` means the card was explicitly confirmed by the agent/user flow.

## Working rules for agents

- Do not invent new entity types when a normal knowledge card is enough.
- Prefer editing or creating cards over writing long summaries in chat.
- Validate before claiming the graph is consistent.
- When adding references, prefer a small number of strong links over many weak
  links.
- Keep cards reasonably atomic. If a card contains multiple independent ideas,
  split it.
- Treat this file as the primary operational entry point for the repository.
- Keep `README.md` short; do not duplicate the full workflow there.

## Bounded retrieval policy

Agents must keep context bounded and graph-first.

- Never read the entire `vault/` by default for a local task.
- Start from one or more seed card IDs or from a bounded search result.
- Build context through graph neighbors first, not raw file scans.
- Default retrieval budget:
  - graph depth: `1`
  - max cards in working context: `8`
  - max chunks opened after graph selection: `3`
  - open the original asset only if card and chunk evidence is insufficient
- Prefer `stable` cards over `draft` cards when both satisfy the same need.
- If the task grows beyond the retrieval budget, create an intermediate
  knowledge card and continue from that card instead of expanding the live
  prompt indefinitely.
- For contradiction work, check explicit `contradict` links first. Only then
  inspect nearby supporting cards or source chunks.
- For synthesis or inference, create a new knowledge card with references to
  the cards it draws from. Do not treat chat output as the durable synthesis.

## Startup and CLI workflow

Run commands from repository root:

```bash
python3 -m philosopher_agent new "Card title"
python3 -m philosopher_agent check
python3 -m philosopher_agent build-graph
python3 -m philosopher_agent check --private-user <username>
python3 -m philosopher_agent build-graph --private-user <username>
python3 -m philosopher_agent search-cards "query"
python3 -m philosopher_agent context-pack <card-id> [<card-id> ...]
python3 -m philosopher_agent link <source-id> <target-id> --relation support
python3 -m philosopher_agent find-contradictions <card-id> [<card-id> ...]
```

Before reporting repository state or graph quality:

- ensure the repository layout exists
- create or edit cards
- run `python3 -m philosopher_agent check`
- run `python3 -m philosopher_agent build-graph`

Use these commands after changing cards:

1. Create or edit cards
2. Run `check`
3. Run `build-graph`
4. Only then report the graph as valid

## Large document ingestion

Never try to load a huge document into one prompt or convert it into one giant
card.

Use this ingestion strategy:

1. Store the original file under `vault/public/assets/` or
   `vault/private/users/<username>/assets/`
2. Extract text into `staging/imports/`
3. Split the text into chunks in `staging/chunks/`
4. Process chunks incrementally
5. Create multiple knowledge cards from the chunks
6. Add references between the resulting cards
7. Build the graph after ingest

### Chunking rules

- Prefer heading-based splits first
- If headings are weak, split by page ranges
- If pages are too dense, split by token budget
- Keep overlap between adjacent chunks for context continuity
- Keep chunk metadata: source file, page range, section title, chunk index

### Output rules for big inputs

- Do not create one card per page by default
- Do not create one card for the whole document by default
- Create cards around coherent ideas, claims, procedures, or arguments
- If needed, create one top-level document card that references the cards
  extracted from that document

See [`docs/large-doc-ingestion.md`](docs/large-doc-ingestion.md) for the
detailed ingest policy.
