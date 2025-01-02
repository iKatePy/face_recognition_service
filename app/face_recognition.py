import cv2
import numpy as np
from fastapi import UploadFile
from .singleton import FaceRecognitionModel  # Импортируем класс Singleton

def detect_faces(uploaded_file: UploadFile):
    """
    Detect faces in an uploaded image using OpenCV.

    Args:
        uploaded_file (UploadFile): The uploaded image file.

    Returns:
        list: List of bounding box coordinates for detected faces.
    """
    # Read the image file into a NumPy array
    image = np.array(bytearray(uploaded_file.file.read()), dtype=np.uint8)
    
    # Decode the image array to an OpenCV format
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Convert image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Используем Singleton для получения модели распознавания лиц
    model = FaceRecognitionModel()
    
    # Detect faces in the image using the model
    faces = model.detect_faces(gray)

    # Prepare list to hold coordinates of detected faces
    face_coordinates = []
    
    # Iterate over detected faces and store their coordinates
    for (x, y, w, h) in faces:
        face_coordinates.append({
            "x": int(x),
            "y": int(y),
            "width": int(w),
            "height": int(h)
        })
    
    return face_coordinates  # Return list of coordinates as output

