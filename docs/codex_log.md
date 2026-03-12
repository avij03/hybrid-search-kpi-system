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

## Prompt 4
Task: Implement semantic vector indexing.

Prompt used:
Implement vector indexing in backend/app/search.py using TF-IDF embeddings and FAISS.

Result:
Created vector.index and vector_meta.pkl for semantic search.

-----------------------------------------------------------------------------------------------------------------------

## Prompt 5
Task: Implement hybrid search API.

Prompt used:
Create a FastAPI service in backend/app/api.py with endpoints:
GET /health
POST /search

The search endpoint should combine BM25 scores and vector similarity scores into a hybrid score using a weighted parameter alpha.

Result:
Implemented FastAPI backend exposing hybrid search functionality and verified results using Swagger UI.

------------------------------------------------------------------------------------------------------------------------

## Prompt 6
Task: Implement dashboard UI.

Prompt used:
Create a Streamlit dashboard in frontend/dashboard.py that allows users to input search queries and visualize hybrid search results.

The dashboard should:
- Accept query input
- Allow tuning of top_k and alpha parameters
- Display results in a table
- Visualize bm25_score, vector_score, and hybrid_score.

Result:
Implemented Streamlit dashboard for interactive hybrid search visualization.

------------------------------------------------------------------------------------------------------------------------

## Prompt 7
Task: Implement evaluation metrics.

Prompt used:
Create evaluation module backend/app/evaluate.py implementing Recall@k and nDCG@k metrics for search performance evaluation.

Result:
Implemented evaluation script and created evaluation dataset data/eval/qrels.json.

------------------------------------------------------------------------------------------------------------------------

## Prompt 8
Task: Expand corpus size to support meaningful evaluation.

Prompt used:
Generate a synthetic corpus of at least 300 short technical documents covering topics such as machine learning, cybersecurity, vector search, and distributed systems. The output should be saved in data/raw so the ingestion pipeline can process it.

Result:
Generated backend/app/generate_docs.py which produces a synthetic corpus of 300 documents.

Action taken:
Re-ran ingestion and indexing pipelines to rebuild the dataset and indexes for evaluation experiments.

-----------------------------------------------------------------------------------------------------------------------

## Prompt 9
Task: Create evaluation dataset for retrieval benchmarking.

Prompt used:
Generate a set of evaluation queries and relevance judgements suitable for testing a hybrid search system.

Result:
Created queries.jsonl with 25 queries and qrels.json mapping queries to relevant documents.

-----------------------------------------------------------------------------------------------------------------------

## Prompt 10
Task: Implement evaluation pipeline and experiment tracking.

Prompt used:
Extend the evaluation script to load queries, call the hybrid search API, compute Recall@10, nDCG@10, and MRR@10, and log results to a CSV file under data/metrics.

Result:
Implemented evaluation loop in evaluate.py and experiment logging to data/metrics/experiments.csv.

-----------------------------------------------------------------------------------------------------------------------

## Prompt 11
Task: Add observability and structured logging to the API.

Prompt used:
Modify the FastAPI search endpoint to generate structured logs including request_id, query parameters, latency, and result counts.

Result:
Implemented structured JSON logging in api.py for every search request.

------------------------------------------------------------------------------------------------------------------------

## Prompt 12
Task: Add persistent query logging using SQLite.

Prompt used:
Implement a SQLite database to store search queries and metrics such as request_id, query text, alpha parameter, latency, result count, and timestamp.

Result:
Created backend/app/db.py for database management and integrated query logging into the FastAPI search endpoint. Each search request is now stored in data/metrics/search_logs.db.

------------------------------------------------------------------------------------------------------------------------

## Prompt 13
Task: Add system KPIs to the Streamlit dashboard.

Prompt used:
Extend the dashboard to show total queries, average latency, and most frequent queries using the SQLite query log database.

Result:
Dashboard now displays KPI metrics from search_logs.db.

------------------------------------------------------------------------------------------------------------------------

## Prompt 14
Task: Design break/fix scenarios for system reliability testing.

Prompt used:
Generate realistic failure scenarios for the hybrid search system and describe how they can be fixed.

Result:
Created break_fix.md documenting index failures, missing corpus issues, and database recovery steps.

------------------------------------------------------------------------------------------------------------------------

## Prompt 15
Task: Add automated tests for the hybrid search system.

Prompt used:
Generate simple pytest tests to validate the FastAPI health endpoint and the hybrid search endpoint. The tests should verify that the API responds correctly and that search results contain the expected scoring fields.

Result:
Created two test files:
- tests/test_api.py for validating the health and search endpoints
- tests/test_search.py for validating scoring outputs

These tests can be executed using:
python -m pytest