# singleton.py
import cv2

class FaceRecognitionModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FaceRecognitionModel, cls).__new__(cls)
            cls._instance.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        return cls._instance

    def detect_faces(self, gray_image):
        """
        Detect faces in a grayscale image.

        Args:
            gray_image (numpy.ndarray): Grayscale image for face detection.

        Returns:
            list: List of bounding box coordinates for detected faces.
        """
        faces = self.face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
        return faces
