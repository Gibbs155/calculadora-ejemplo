import pytest
import json
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_basic_greeting(client):
    """Test basic greeting endpoint"""
    response = client.get('/api/v1/greeting')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Hello, World!' in data['message']

def test_personalized_greeting(client):
    """Test personalized greeting"""
    response = client.get('/api/v1/greeting?name=TechCorp')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Hello, TechCorp!' in data['message']