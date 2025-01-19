Introduction
This microservice utilizes OpenCV and FastAPI to detect faces in images. Users can upload images via an API, and the service will return the coordinates of detected faces.
Applied the Singleton pattern to manage the face recognition model. This will improve a performance of the application by reducing memory usage and loading time for the model. Every time the detect_faces function is called, the same instance of the model will be used.
Technologies
Please see the requirements.txt for details.
Project Setup
Requirements

    Hardware: Any machine capable of running Python and the required libraries.
    Software:
        Python 3.8 or higher
        PostgreSQL database server

Installation Steps

    Clone the repository:

bash
git clone https://github.com/iKatePy/face_recognition_service.git
cd face_recognition_service

Install required packages:

bash
pip install -r requirements.txt

Set up your PostgreSQL database:

    Create a database named dbname.
    Update the DATABASE_URL in database.py with your credentials.

Run the application:

    bash
    uvicorn app.main:app --reload

    Access the API documentation at http://127.0.0.1:8000/docs.

Usage
To detect faces, send a POST request to the /detect/ endpoint with an image file:

bash
curl -X POST "http://127.0.0.1:8000/detect/" -F "file=@path_to_your_image.jpg"

or press the POST button and then choose a file with the browse button; the file name must be Source.jpg. Then press the Execute button and see the result in Responses. The response will include coordinates of detected faces. You can download a JSON file with coordinates by pressing the 'download' button.
Testing
Created three types of tests for this project:

    The first test simulates uploading an image to the /detect/ endpoint of the FastAPI application. It checks:
        If the response status code is 200, indicating a successful request.
        If the response JSON contains a key named "faces", which suggests that face detection was performed successfully.
    The second test focuses on the internal function detect_faces. It:
        Reads a valid image into memory.
        Creates a mock UploadFile instance to simulate file upload.
        Asserts that the result is a list and that each item in the list is a dictionary, indicating successful face detection.
    The third test measures the performance of the /detect/ endpoint. It:
        Records the start time before making a POST request to upload an image.
        Asserts that the response status code is 200.
        Checks that the duration of the request is less than 2 seconds, ensuring that the endpoint performs efficiently.
        To run tests using pytest, execute:

bash
pytest tests/
