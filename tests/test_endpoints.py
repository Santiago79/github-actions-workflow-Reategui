from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum_endpoint():
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_resta_endpoint():
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_mult_endpoint():
    response = client.post("/mult", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}