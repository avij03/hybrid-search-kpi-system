from fastapi import FastAPI
import pickle
import json
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
import time
import uuid
from datetime import datetime

app = FastAPI()

# Load BM25 index
with open("data/index/bm25.pkl", "rb") as f:
    bm25_data = pickle.load(f)

bm25 = bm25_data["index"]
docs = bm25_data["docs"]

# Load vector index
vector_index = faiss.read_index("data/index/vector.index")

with open("data/index/vector_meta.pkl", "rb") as f:
    vector_meta = pickle.load(f)

vectorizer = vector_meta["vectorizer"]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/search")
def search(query: str, top_k: int = 5, alpha: float = 0.5):

    # Observability start
    request_id = str(uuid.uuid4())
    start_time = time.time()

    tokens = query.lower().split()

    bm25_scores = bm25.get_scores(tokens)

    query_vec = vectorizer.transform([query]).toarray().astype("float32")
    D, I = vector_index.search(query_vec, top_k)

    results = []

    for rank, doc_id in enumerate(I[0]):

        vector_score = 1 / (1 + D[0][rank])
        bm25_score = bm25_scores[doc_id]

        hybrid_score = alpha * bm25_score + (1 - alpha) * vector_score

        results.append({
            "doc_id": docs[doc_id]["doc_id"],
            "text": docs[doc_id]["text"],
            "bm25_score": float(bm25_score),
            "vector_score": float(vector_score),
            "hybrid_score": float(hybrid_score)
        })

    results = sorted(results, key=lambda x: x["hybrid_score"], reverse=True)

    # Observability end
    latency_ms = int((time.time() - start_time) * 1000)

    log_entry = {
        "request_id": request_id,
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "top_k": top_k,
        "alpha": alpha,
        "latency_ms": latency_ms,
        "result_count": len(results)
    }

    print(json.dumps(log_entry))

    return {
        "request_id": request_id,
        "results": results
    }