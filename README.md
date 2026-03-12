Hybrid Search + KPI Dashboard
Overview

This project implements a hybrid search system that combines:

-> BM25 lexical search (keyword matching)

-> Vector semantic search (similarity-based retrieval)

The system retrieves relevant documents using both approaches and combines them through a hybrid scoring mechanism. A dashboard interface is provided to visualize search results and score contributions.

The project demonstrates a complete pipeline including:

1. Data ingestion

2. Index creation

3. Hybrid search API

4. Interactive dashboard

5. Evaluation metrics

System Architecture

The search pipeline works as follows:

Raw Documents
      ↓
Ingestion Pipeline
      ↓
JSONL Document Store
      ↓
BM25 Index (Lexical Search)
      ↓
Vector Index (Semantic Search)
      ↓
Hybrid Search API
      ↓
Dashboard Visualization

----------------------------------------------------------------------------------------------------------------------

Project Structure

backend/app
    ingest.py        → Data ingestion pipeline
    index.py         → BM25 index builder
    search.py        → Vector index builder
    api.py           → Hybrid search API
    evaluate.py      → Evaluation metrics

frontend
    dashboard.py     → Streamlit dashboard

data
    raw              → Raw text documents
    processed        → Normalized JSONL documents
    index            → Search indexes
    eval             → Evaluation dataset

docs
    codex_log.md     → Prompt log of AI-assisted development

tests                → Test directory (reserved)

requirements.txt     → Python dependencies
up.sh                → One-command system startup
break_fix.md         → Break/fix scenarios
README.md            → Project documentation

------------------------------------------------------------------------------------------------------------------------

Components

1. Data Ingestion

Location: backend/app/ingest.py

Reads raw .txt files from: data/raw

and converts them into normalized JSONL records stored in:

data/processed/docs.jsonl

Each document contains:

-> doc_id
-> title
-> text
-> source
-> created_at

2. BM25 Index (Lexical Search)

Location: backend/app/index.py

Builds a BM25 lexical index using the processed document corpus.

Output: data/index/bm25.pkl

BM25 enables fast keyword-based retrieval.

3. Vector Index (Semantic Search)

Location: backend/app/search.py

Creates vector representations of documents using TF-IDF embeddings and builds a FAISS vector index.

Outputs:

data/index/vector.index
data/index/vector_meta.pkl

This enables semantic similarity search.

4. Hybrid Search API

Location: backend/app/api.py

Provides a FastAPI service with the following endpoints:

GET  /health
POST /search

The /search endpoint returns ranked documents using a hybrid scoring formula:

hybrid_score = alpha * bm25_score + (1 - alpha) * vector_score

Where:

alpha = weighting parameter between lexical and semantic search

5. Dashboard Interface

Location: frontend/dashboard.py

Implemented using Streamlit.

Features:

-> Query input field

-> Adjustable top_k results

-> Adjustable alpha hybrid weight

-> Results table

-> Visualization of:

    1. BM25 score

    2. Vector score

    3. Hybrid score

Dashboard runs at: http://localhost:8501

6. Evaluation Metrics

Location: backend/app/evaluate.py

Implements standard information retrieval metrics:

Recall@K
nDCG@K

These metrics help evaluate the quality of the hybrid search system.

Running the System

Step 1 — Start the API
python -m uvicorn backend.app.api:app --reload

API documentation will be available at: http://127.0.0.1:8000/docs

Step 2 — Start the Dashboard
python -m streamlit run frontend/dashboard.py

Open the dashboard: http://localhost:8501

One-Command Startup
You can start the entire system using: bash up.sh

This script launches:

-> FastAPI backend

-> Streamlit dashboard

Break / Fix Scenarios

Common failure scenarios and recovery steps are documented in: break_fix.md

Examples include:

-> Missing BM25 index

-> Missing processed documents

-> API server not running

AI-Assisted Development

Development prompts used during the project are recorded in: docs/codex_log.md

The prompt log documents:

    1. repository setup
    2. ingestion pipeline generation
    3. BM25 indexing
    4. vector indexing
    5. API implementation
    6. dashboard development
    7. evaluation metrics

Tech Stack:
-> Python
-> FastAPI
-> Streamlit
-> FAISS
-> rank-bm25
-> scikit-learn
-> NumPy
-> Pandas

Summary

This project demonstrates a complete hybrid search system including:

1. ingestion pipeline

2. lexical retrieval

3. semantic retrieval

4. hybrid scoring

5. API service

6. visualization dashboard

7. evaluation metrics

The system shows how combining lexical and semantic search improves retrieval performance.

## Quick Start

Run the entire system with:

./up.sh

This will:

- generate the dataset
- build indexes
- start the FastAPI backend
- launch the Streamlit dashboard