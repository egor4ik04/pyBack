'''Корневой файл проекта FastAPI'''

import uuid # генерация guid
import shutil # копирование файлов (для загрузки)

from fastapi import (
    FastAPI, # корень программы
    Request, # объект Request - для получения информации о запросе (пр. - загаловки)
    Response, # объект Response - инфо об ответе обработанного запроса
    Cookie, # доступ к кукам
    Form, # доступ к данным формы
    File, # обмен файлами в запросах
    UploadFile
)
from fastapi.responses import (
    HTMLResponse, # отправка в response htmlcontent
    FileResponse, # загрузка клиенту файла
    RedirectResponse, # ответ-перенаправление
)
from fastapi.staticfiles import StaticFiles # подключение директории статичных файлов (строка 13)
from pydantic import (
    BaseModel, # наследники выступают как расшифровываемая модель входных данных
    Field, # для детальной настройки атрибутов модели
)

# Работа с классами:
#   Создайте класс User с полями id, username, email и password.
class User(BaseModel):
    """Класс для представления пользователя."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str = Field(..., min_length=3, max_length=20)
    email: str = Field(...)
    password: str = Field(..., min_length=6)

users_db = [
    User(username="testuser1", email="test1@test.com", password="password1"),
    User(username="testuser2", email="test2@test.com", password="password2"),
    User(username="testuser3", email="test3@test.com", password="password3"),
]

app = FastAPI()

app.mount("/static", StaticFiles(directory="public", html=True))
# Можно перейти по статическим файлам проекта. Пример - http://127.0.0.1:8000/static/
# Указывается либо конкретный файл, либо как в примере возврат по умолчанию index.html

# Создание базового API:
#   Определите маршрут / с помощью декоратора @app.get("/"),
#   который будет возвращать простое сообщение "Hello, World!".
@app.get("/")
def root():
    '''Вывод Hello, World в корневом адресе.'''
    return HTMLResponse(content="<h1>Hello, World!</h1>")
# Пробный маршрут - http://127.0.0.1:8000/


# Обработка параметров:
#   Создайте маршрут /greet/{name}, который принимает
#   параметр пути name и возвращает приветствие "Hello, {name}!".
@app.get("/greet/{name}")
def greet(name: str):
    '''Приветствие пользователя.'''
    return {"message": f"Hello, {name}!"}
# Пробный маршрут - http://127.0.0.1:8000/greet/test

#   Создайте маршрут /search, который принимает
#   параметр строки запроса query и возвращает сообщение "You searched for: {query}".
@app.get("/search")
def search(query: str):
    '''Получение параметра запроса поиска через строку запроса.'''
    return {"message": f"You searched for: {query}"}
# Пробный маршрут - http://127.0.0.1:8000/search?query=test


# Отправка различных типов данных:
#   Создайте маршрут /json, который возвращает JSON-ответ с данными о вас (имя, возраст, хобби).
@app.get("/json")
def get_json():
    '''(Не)Мои данные в формате json.'''
    return {"name": "NotEgor", "age": 20, "hobbies": ["coding", "gaming", "reading"]}
# Пробный маршрут - http://127.0.0.1:8000/json

#   Создайте маршрут /file, который отправляет текстовый файл с произвольным содержимым.
@app.get("/file")
def get_file():
    '''Отправка файла с шагами по начальной настройке проекта и работе с FastAPI.'''
    file_path = "public/steps.txt"
    return FileResponse(file_path, media_type="text/plain", filename="steps.txt")
# Пробный маршрут - http://127.0.0.1:8000/file

#   Создайте маршрут /redirect, который выполняет перенаправление на маршрут /.
@app.get("/redirect")
def redirect_to_home():
    '''Перенаправление на главную страницу.'''
    return RedirectResponse(url="/")
# Пробный маршрут - http://127.0.0.1:8000/redirect


# Работа с заголовками и куками:
#   Создайте маршрут /headers, который возвращает все заголовки запроса в виде JSON.
@app.get("/headers")
def read_headers(request: Request):
    """Возвращает все заголовки запроса в виде JSON."""
    return {"headers": dict(request.headers)}
# Пробный маршрут - http://127.0.0.1:8000/headers

#   Создайте маршрут /set-cookie, который устанавливает куку
#   с именем username и значением your_name.
@app.get("/set-cookie")
def set_cookie(response: Response):
    """Устанавливает куку с именем username и значением your_name."""
    response.set_cookie(key="username", value="your_name")
    return {"message": "Cookie has been set"}
# Пробный маршрут - http://127.0.0.1:8000/set-cookie

#   Создайте маршрут /get-cookie, который возвращает значение куки username.
@app.get("/get-cookie")
def get_cookie(username: str = Cookie()):
    """Возвращает значение куки username."""
    if username:
        return {"username": username}
    return {"message": "Cookie not found"}
# Пробный маршрут - http://127.0.0.1:8000/get-cookie
# В браузере в Application-Cookies-http://127.0.0.1:8000 куки записаны

# Обработка данных запроса:
#   Создайте маршрут /login, который принимает данные формы с полями
#   username и password и возвращает сообщение "Welcome, {username}!".
@app.post("/login")
def login(
    username: str = Form(..., min_length=3, max_length=20),
    password: str = Form(..., min_length=6, max_length=20)
):
    """Принимает данные формы и приветствует пользователя."""
    # Проверяем на пустоту или пробелы
    if not username.strip() or not password.strip():
        return {"message": "Username or password cannot be empty"}
    return {"message": f"Welcome, {username}!"}
# для доступа ниже создана страница с формой (или через Postman)

#   Создайте маршрут /register, который принимает JSON-данные с полями
#   username, email и password и возвращает сообщение "User {username} registered successfully!".
@app.post("/register")
def register(
    username: str = Form(..., min_length=3, max_length=30),
    email: str = Form(..., pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
    password: str = Form(..., min_length=6)
):
    """Регистрирует нового пользователя на основе JSON-данных."""
    if not username.strip() or not email.strip() or not password.strip():
        return {"message": "Fields cannot be empty"}
    return {"message": f"User {username} registered successfully!"}
# для доступа ниже создана страница с формой (или через Postman)

@app.get("/login-form")
async def login_page():
    """Возвращает HTML-страницу для входа."""
    return FileResponse("public/login.html")
# Пробный маршрут - http://127.0.0.1:8000/login-form

@app.get("/register-form")
async def register_page():
    """Возвращает HTML-страницу для регистрации."""
    return FileResponse("public/register.html")
# Пробный маршрут - http://127.0.0.1:8000/register-form


# Работа с классами:
#   Создайте маршрут /users, который возвращает список объектов класса User в формате JSON.
@app.get("/users")
def get_users():
    """Возвращает список всех пользователей."""
    return users_db
# Пробный маршрут - http://127.0.0.1:8000/users

#   Создайте маршрут /users/{id}, который возвращает объект класса User с указанным id.
@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    """Возвращает пользователя по его ID."""
    result = None
    for user in users_db:
        if str(user.id) == user_id:
            result = user
    if result is None:
        return {"message": f"User with id {user_id} not found"}
    return result
# Пробный маршрут - http://127.0.0.1:8000/users/{guid}
# Примерно будет при генерации выглядеть так: ea1f0542-4266-436f-a963-d2f1c66e3656


# Дополнительные задания (по желанию):
#   Реализуйте валидацию данных на маршрутах /login и /register.
# Импортированный класс Form позволяет задать валидацию данных в параметрах метода.
# Таким образом я заменил логин с параметров, просто принимающих из формы данные:
# def login(username: str = Form(...), password: str = Form(...)):
# на текущие:
# def login(
#     username: str = Form(..., min_length=3, max_length=20),
#     password: str = Form(..., min_length=6, max_length=20)
# ):

#   Добавьте возможность загрузки файлов на сервер.
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    """Загружает файл на сервер и сохраняет его."""
    file_location = f"public/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File uploaded successfully!"}
# Для доступа к post-запросу снова использую html страницу:
@app.get("/upload-form")
async def upload_form():
    """Возвращает форму для загрузки файла."""
    return FileResponse("public/upload_form.html")
# Пробный маршрут - http://127.0.0.1:8000/upload-form
# После выбора и отправки увидим сообщение
# {"filename":"имя_файла","message":"File uploaded successfully!"}
# Далее откроем его в http://127.0.0.1:8000/static/имя_файла
