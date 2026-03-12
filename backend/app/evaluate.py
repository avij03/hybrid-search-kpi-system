import json
import numpy as np
import requests
import csv
from datetime import datetime
import subprocess


API_URL = "http://127.0.0.1:8000/search"
K = 10


def recall_at_k(relevant, retrieved, k):
    retrieved_k = retrieved[:k]
    return len(set(relevant) & set(retrieved_k)) / len(relevant)


def ndcg_at_k(relevant, retrieved, k):
    dcg = 0
    for i, doc in enumerate(retrieved[:k]):
        if doc in relevant:
            dcg += 1 / np.log2(i + 2)

    idcg = sum(1 / np.log2(i + 2) for i in range(min(len(relevant), k)))

    return dcg / idcg if idcg > 0 else 0


def mrr_at_k(relevant, retrieved, k):
    for i, doc in enumerate(retrieved[:k]):
        if doc in relevant:
            return 1 / (i + 1)
    return 0


def load_queries():
    queries = []

    with open("data/eval/queries.jsonl") as f:
        for line in f:
            queries.append(json.loads(line))

    return queries


def load_qrels():
    with open("data/eval/qrels.json") as f:
        return json.load(f)


def run_evaluation(alpha=0.5):

    queries = load_queries()
    qrels = load_qrels()

    recall_scores = []
    ndcg_scores = []
    mrr_scores = []

    for q in queries:

        query_id = str(q["query_id"])
        query_text = q["query"]

        response = requests.post(
            API_URL,
            params={"query": query_text, "top_k": K, "alpha": alpha}
        )

        results = response.json()["results"]

        retrieved = [r["doc_id"] for r in results]
        relevant = qrels.get(query_id, [])

        recall_scores.append(recall_at_k(relevant, retrieved, K))
        ndcg_scores.append(ndcg_at_k(relevant, retrieved, K))
        mrr_scores.append(mrr_at_k(relevant, retrieved, K))

    recall = np.mean(recall_scores)
    ndcg = np.mean(ndcg_scores)
    mrr = np.mean(mrr_scores)

    print("Recall@10:", recall)
    print("nDCG@10:", ndcg)
    print("MRR@10:", mrr)

    log_experiment(alpha, ndcg, recall, mrr)


def log_experiment(alpha, ndcg, recall, mrr):

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
    except:
        commit = "unknown"

    row = [
        datetime.now().isoformat(),
        alpha,
        "tfidf-faiss",
        round(ndcg, 4),
        round(recall, 4),
        round(mrr, 4),
        commit
    ]

    with open("data/metrics/experiments.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


if __name__ == "__main__":
    run_evaluation(alpha=0.5)