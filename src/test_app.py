import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_add(client):
    response = client.get('/add?a=5&b=3')
    assert response.status_code == 200
    assert response.get_json() == {"result": 8.0}

def test_subtract(client):
    response = client.get('/subtract?a=10&b=4')
    assert response.status_code == 200
    assert response.get_json() == {"result": 6.0}

def test_invalid_input(client):
    response = client.get('/add?a=x&b=3')
    assert response.status_code == 400
    assert "error" in response.get_json()
