# Break / Fix Scenarios

## Scenario 1 – Missing BM25 index

Break:
Delete data/index/bm25.pkl

Expected issue:
Search API fails because BM25 index cannot be loaded.

Fix:
Rebuild the index by running:

python -m backend.app.index --input data/processed/docs.jsonl --out data/index


## Scenario 2 – Missing processed documents

Break:
Delete data/processed/docs.jsonl

Expected issue:
Index building fails because the processed corpus is missing.

Fix:
Run ingestion again:

python -m backend.app.ingest --input data/raw --out data/processed


## Scenario 3 – API not running

Break:
Stop the FastAPI server.

Expected issue:
Dashboard cannot fetch search results.

Fix:
Restart the API:

python -m uvicorn backend.app.api:app --reload