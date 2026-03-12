# Break / Fix Scenarios

## Scenario 1 – Missing BM25 Index

Break:
Delete data/index/bm25.pkl

Effect:
FastAPI server fails to start because the BM25 index cannot be loaded.

Fix:
Rebuild the index:

python -m backend.app.index --input data/processed/docs.jsonl --out data/index


## Scenario 2 – Missing Processed Documents

Break:
Delete data/processed/docs.jsonl

Effect:
Indexing fails because the processed corpus does not exist.

Fix:
Run ingestion pipeline:

python -m backend.app.ingest --input data/raw --out data/processed

Then rebuild indexes.


## Scenario 3 – Missing SQLite Database

Break:
Delete data/metrics/search_logs.db

Effect:
Dashboard KPIs fail because query logs are missing.

Fix:
Restart the API. The database is automatically recreated by the init_db() function.