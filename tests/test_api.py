from fastapi.testclient import TestClient  # Import TestClient for testing FastAPI apps
from app.main import app  # Import FastAPI app instance

client = TestClient(app)  # Create a test client instance

def test_detect_faces():
    """
    Test case for detecting faces in an uploaded image.

    This test simulates uploading an image and checks if the response is valid.
    """
    
    with open("Source.jpg", "rb") as img_file:  # Open a sample image file in binary mode
        response = client.post("/detect/", files={"file": img_file})  # Send POST request to /detect endpoint
        
        assert response.status_code == 200  # Check if response status is OK (200)
        assert "faces" in response.json()  # Ensure 'faces' key is present in JSON response
        
