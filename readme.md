# Face Recognition Microservice

## Introduction / Введение
This microservice utilizes OpenCV and FastAPI to detect faces in images. Users can upload images via an API, and the service will return the coordinates of detected faces. 
Applied the Singleton pattern to manage the face recognition model. This will improve a performance of the application by reducing memory usage and loading time for the model. Every time the detect_faces function is called, the same instance of the model will be used. 


Этот микросервис использует OpenCV и FastAPI для обнаружения лиц на изображениях. Пользователи могут загружать изображения через API, и сервис будет возвращать координаты обнаруженных лиц. Применен шаблон Singleton для управления моделью распознавания лиц. Это улучшит производительность приложения за счет сокращения использования памяти и времени загрузки модели. Каждый раз при вызове функции detect_faces будет использоваться один и тот же экземпляр модели.

## Technologies 
Pls see the requirements.txt 

Пожалуйста, посмотрите requirements.txt

## Project Setup

### Requirements / Требования
- **Hardware**: Any machine capable of running Python and the required libraries.
- Любое оборудование, поддерживающее версии Python и библиотек, представленных в requirements.txt
- **Software** / ПО:
  - Python 3.8 or higher
  - PostgreSQL database server

### Installation Steps / Этапы установки
1. Clone the repository:
   Клонирование репозитория:

git clone https://github.com/iKatePy/face_recognition_service.git
cd face_recognition_service

2. Install required packages:
   
   Установка пакетов из файла requirements.txt:
   
pip install -r requirements.txt


3. Set up your PostgreSQL database:
   
   Настройка базы данных PostgreSQL database:
   
- Create database named `dbname`.
- Создать базу данных с названием `dbname`
  
- Update the `DATABASE_URL` in `database.py` with your credentials.
- В файле `database.py` заменить в строке `DATABASE_URL` данные логин, пароль, название таблицы (если оно отличное от "dbname")

4. Run the application:
   
   Запуск приложения - выполнить команду:
   
   uvicorn app.main:app --reload


6. Access the API documentation at `http://127.0.0.1:8000/docs`.
   
   Перейти по адресу `http://127.0.0.1:8000/docs` для доступа к документации API 

## Usage / Применение
- To detect faces, send a POST request to the `/detect/` endpoint with an image file:

curl -X POST "http://127.0.0.1:8000/detect/" -F "file=@path_to_your_image.jpg"

or press POST button and then choose a file with browse button, file name must be 1.jpg, 
then press Execute button and see the result in Responses

The response will include coordinates of detected faces.

You can download JSON file with coordinates by pressing 'download' button

- Для обнаружения лиц отправьте запрос POST на конечную точку `/detect/` с файлом изображения:

curl -X POST "http://127.0.0.1:8000/detect/" -F "file=@path_to_your_image.jpg"

или нажмите кнопку POST, а затем выберите файл кнопкой обзора, имя файла должно быть "1.jpg",
затем нажмите кнопку Execute и посмотрите результат в Responses

Ответ будет включать координаты обнаруженных лиц.

Вы можете загрузить файл JSON с координатами, нажав кнопку «download»

## Testing / Тестирование
- Created 3 types of tests for this project: 
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
pytest tests/

- Создано 3 типа тестов для этого проекта:
Первый тест имитирует загрузку изображения в конечную точку /detect/ приложения FastAPI. Он проверяет:
Соответствует ли код статуса ответа 200, что указывает на успешный запрос.
Содержит ли ответ JSON ключ с именем «faces», что говорит об успешном выполнении распознавания лиц.
Второй тест фокусируется на внутренней функции detect_faces. Он:
Считывает допустимое изображение в память.
Создает фиктивный экземпляр UploadFile для имитации загрузки файла.
Утверждает, что результатом является список, а каждый элемент в списке — словарь, что указывает на успешное обнаружение лиц.
Третий тест измеряет производительность конечной точки /detect/. Он:
Записывает время начала перед выполнением запроса POST для загрузки изображения.
Убеждается, что код статуса ответа — 200.
Проверяет, что длительность запроса составляет менее 2 секунд, что гарантирует эффективную работу конечной точки.
Чтобы запустить тесты с помощью pytest, выполните:
pytest tests/




