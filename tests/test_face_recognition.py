import pytest
from fastapi import UploadFile
from io import BytesIO
from app.face_recognition import detect_faces

def test_detect_faces_valid_image():
    # Load a valid image into memory
    with open("tests/1.jpg", "rb") as f:
        image_data = f.read()
    
    # Create a mock UploadFile instance
    upload_file = UploadFile(filename="1.jpg", file=BytesIO(image_data))
    
    result = detect_faces(upload_file)
    
    assert isinstance(result, list)  # Ensure it returns a list
    assert all(isinstance(face, dict) for face in result)  # Each face should be a dictionary
