import requests


def test_search_returns_scores():

    response = requests.post(
        "http://127.0.0.1:8000/search",
        params={
            "query": "cybersecurity",
            "top_k": 5,
            "alpha": 0.5
        }
    )

    results = response.json()["results"]

    first = results[0]

    assert "bm25_score" in first
    assert "vector_score" in first
    assert "hybrid_score" in first