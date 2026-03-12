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

## Prompt 2
Task: Implement ingestion pipeline.

Prompt used:
Implement backend/app/ingest.py that reads .txt files from data/raw and converts them into JSONL format with fields:
doc_id, title, text, source, created_at.

The script should run as:
python -m backend.app.ingest --input data/raw --out data/processed

Result:
Generated ingestion module that normalizes documents and saves them to data/processed/docs.jsonl.