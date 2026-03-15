# Large Document Ingestion

This repository should treat large inputs as a staged pipeline, not as a single
LLM prompt.

## Goal

Turn a large document into a set of connected knowledge cards without losing
traceability or blowing up the context window.

## Pipeline

### 1. Stage the source

- Save the original file under the correct assets directory
- Public files go to `vault/public/assets/`
- Local-only files go to `vault/private/users/<username>/assets/`

### 2. Extract raw text

- Convert the source into text or Markdown
- Save the extracted output in `staging/imports/`
- Preserve basic metadata where possible: filename, page numbers, headings

### 3. Chunk the extracted text

Chunk using this fallback order:

1. Heading sections
2. Page ranges
3. Token windows with overlap

Recommended defaults:

- Target chunk size: `800-1800` tokens
- Overlap: `10-15%`
- Cap very large sections before they hit the model window

Each chunk should keep:

- `source_path`
- `visibility`
- `page_start`
- `page_end`
- `section_title`
- `chunk_index`

### 4. Extract candidate knowledge

For each chunk:

- identify atomic ideas
- write or update knowledge cards
- attach references only when justified by the chunk or by already stable cards

### 5. Consolidate across chunks

After chunk-level extraction:

- merge duplicate candidate cards
- normalize titles and IDs
- add cross-chunk references
- mark cards `draft` until reviewed

### 6. Build a document-level entry point

If the source is important, create one top-level knowledge card representing
the document as a whole. Its job is navigation, not storing the entire text.

That card should:

- summarize the document at a high level
- reference major extracted cards
- point to the asset path in the body if useful

## Practical guidance for agents

- Read only the chunks needed for the current task
- Prefer breadth-first scanning first, then deep extraction in relevant areas
- Do not send dozens of raw chunks into one model call
- When the user asks a narrow question, only ingest the relevant sections
- When uncertain, produce fewer higher-quality cards instead of many weak ones

## Why this works

- Keeps prompts bounded
- Preserves provenance
- Fits the repository's graph model
- Avoids giant unreadable Markdown cards
