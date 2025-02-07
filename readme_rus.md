Введение
Этот микросервис использует OpenCV и FastAPI для обнаружения лиц на изображениях. Пользователи могут загружать изображения через API, и сервис вернёт координаты обнаруженных лиц.
Применён шаблон Singleton для управления моделью распознавания лиц, что улучшит производительность приложения за счёт уменьшения использования памяти и времени загрузки модели. Каждый раз, когда вызывается функция detect_faces, используется один и тот же экземпляр модели.
Технологии
Подробности можно посмотреть в файле requirements.txt.
Настройка проекта
Требования

    Аппаратное обеспечение: Любая машина, способная запускать Python и необходимые библиотеки.
    Программное обеспечение:
        Python 3.8 или выше
        Сервер базы данных PostgreSQL

Шаги установки

    Клонировать репозиторий:

bash
git clone https://github.com/iKatePy/face_recognition_service.git
cd face_recognition_service

Установить необходимые пакеты:

bash
pip install -r requirements.txt

Настроить сервер базы данных PostgreSQL:

    Создать базу данных с именем dbname.
    Обновить DATABASE_URL в database.py с вашими учетными данными.

Запустить приложение:

    bash
    uvicorn app.main:app --reload

    Доступ к документации API по адресу http://127.0.0.1:8000/docs.

Использование
Чтобы обнаружить лица, отправьте POST-запрос на конечную точку /detect/ с файлом изображения:

bash
curl -X POST "http://127.0.0.1:8000/detect/" -F "file=@path_to_your_image.jpg"

или нажмите кнопку POST, затем выберите файл с помощью кнопки «Обзор»; имя файла должно быть Source.jpg. Затем нажмите кнопку «Execute(Выполнить)» и посмотрите результат в разделе «Responses(Ответы)». Ответ будет содержать координаты обнаруженных лиц. Вы можете скачать файл JSON с координатами, нажав кнопку «download (Скачать)».
Тестирование
Созданы три типа тестов для этого проекта:

    Первый тест имитирует загрузку изображения на конечную точку /detect/ приложения FastAPI. Он проверяет:
        Если код состояния ответа равен 200, что указывает на успешный запрос.
        Если в JSON-ответе содержится ключ с именем "faces", что указывает на успешное обнаружение лиц.
    Второй тест фокусируется на внутренней функции detect_faces. Он:
        Читает в память допустимое изображение.
        Создаёт имитированный экземпляр UploadFile, чтобы симулировать загрузку файла.
        Утверждает, что результатом является список, и каждый элемент списка — словарь, что указывает на успешное обнаружение лиц.
    Третий тест измеряет производительность конечной точки /detect/. Он:
        Записывает время начала перед отправкой POST-запроса для загрузки изображения.
        Утверждает, что код состояния ответа равен 200.
        Проверяет, что продолжительность запроса меньше 2 секунд, что гарантирует эффективную работу конечной точки.
        Чтобы запустить тесты с помощью pytest, выполните:

bash
pytest tests/
