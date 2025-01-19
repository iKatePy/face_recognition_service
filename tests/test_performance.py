import pytest
import time
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import based on your project structure

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_performance_detect_faces(client):
    start_time = time.time()
    response = client.post("/detect/", files={"file": ("Source.jpg", open("Source.jpg", "rb"))})
    duration = time.time() - start_time
    
    assert response.status_code == 200
    assert duration < 2.0  # Ensure it responds within 2 seconds
