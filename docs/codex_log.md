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