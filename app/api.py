from fastapi import APIRouter, File, UploadFile
from .face_recognition import detect_faces
from .decorators import log_file_upload  # Import the decorator

# Create an API router instance
router = APIRouter()

@router.post("/detect/")
@log_file_upload  # Apply the decorator here
async def detect_faces_endpoint(file: UploadFile = File(...)):
    """
    Endpoint to upload an image and detect faces.
    
    Args:
        file (UploadFile): Image file uploaded by user.

    Returns:
        dict: Coordinates of detected faces.
    """
    results = detect_faces(file)  # Call face detection function with uploaded file
    return {"faces": results}  # Return detected face coordinates as JSON response

