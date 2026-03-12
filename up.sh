echo "Starting Hybrid Search System..."

echo "Starting FastAPI API..."
python -m uvicorn backend.app.api:app --reload &

echo "Starting Streamlit Dashboard..."
python -m streamlit run frontend/dashboard.py