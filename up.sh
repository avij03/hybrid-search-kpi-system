#!/bin/bash

echo "Starting Hybrid Search System Setup..."

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating synthetic corpus..."
python backend/app/generate_docs.py

echo "Running ingestion pipeline..."
python -m backend.app.ingest --input data/raw --out data/processed

echo "Building BM25 index..."
python -m backend.app.index --input data/processed/docs.jsonl --out data/index

echo "Building vector index..."
python -m backend.app.search --input data/processed/docs.jsonl --out data/index

echo "Starting FastAPI server..."
uvicorn backend.app.api:app --reload &

sleep 3

echo "Launching Streamlit dashboard..."
streamlit run frontend/dashboard.py

echo "System is running!"