import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_get_jobs(client):
    response = client.get('/jobs')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_job(client):
    payload = {
        "company": "OpenAI",
        "position": "AI Engineer",
        "location": "Remote", 
        "salary": 100000,
        "status": "applied",
        "notes": "Looking forward to the role!",       
    }

    response = client.post('/jobs', json=payload)
    assert response.status_code == 201
    assert response.json['message'] == 'Job added successfully!'





        