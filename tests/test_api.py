import requests


def test_health_endpoint():
    response = requests.get("http://127.0.0.1:8000/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_search_endpoint():
    response = requests.post(
        "http://127.0.0.1:8000/search",
        params={
            "query": "machine learning",
            "top_k": 5,
            "alpha": 0.5
        }
    )

    data = response.json()

    assert response.status_code == 200
    assert "results" in data
    assert len(data["results"]) > 0