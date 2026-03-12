# Codex Prompt Log

## Prompt 1
Task: Initialize repository structure for hybrid search + KPI dashboard system.

Folders created:
backend/app
frontend
data/raw
data/processed
data/index
data/eval
data/metrics
docs
tests

Action:
Created directories using mkdir commands in Windows CMD.

------------------------------------------------------------------------------------------------------------------------

## Prompt 2
Task: Implement ingestion pipeline.

Prompt used:
Implement backend/app/ingest.py that reads .txt files from data/raw and converts them into JSONL format with fields:
doc_id, title, text, source, created_at.

The script should run as:
python -m backend.app.ingest --input data/raw --out data/processed

Result:
Generated ingestion module that normalizes documents and saves them to data/processed/docs.jsonl.

Edits made:
Reviewed the generated code and kept the document parsing logic and JSONL output implementation.

----------------------------------------------------------------------------------------------------------

## Prompt 3
Task: Implement BM25 indexing.

Prompt used:
Implement BM25 indexing in backend/app/index.py using rank-bm25.
Load documents from data/processed/docs.jsonl and build BM25 index over title and text fields.
Save index to data/index/bm25.pkl.

Result:
Generated BM25 indexing module and created lexical search index artifact.

------------------------------------------------------------------------------------------------------------------------

