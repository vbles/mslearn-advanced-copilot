import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_cities_for_spain():
    response = client.get('/countries/Spain')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # Add more assertions based on the expected data structure