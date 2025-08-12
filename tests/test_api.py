from fastapi.testclient import TestClient
from main import app
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

client = TestClient(app)
headers = {"X-API-Key": "secret123"}


def test_pow():
    response = client.post("/pow", json={"a": 2, "b": 3}, headers=headers)
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_fibonacci():
    response = client.post("/fibonacci", json={"a": 10}, headers=headers)
    assert response.status_code == 200
    assert response.json()["result"] == 55


def test_factorial():
    response = client.post("/factorial", json={"a": 5}, headers=headers)
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_history_requires_auth():
    response = client.get("/history")
    assert response.status_code == 401
