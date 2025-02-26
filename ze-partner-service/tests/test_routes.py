from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_partner():
    response = client.post("/partners", json={
        "tradingName": "Test",
        "ownerName": "Owner",
        "document": "123",
        "coverageArea": {"type": "MultiPolygon", "coordinates": [[[[0, 0], [1, 1], [1, 0], [0, 0]]]]},
        "address": {"type": "Point", "coordinates": [0, 0]}
    })
    assert response.status_code == 200
    assert response.json()["tradingName"] == "Test"