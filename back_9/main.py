'''Корневой файл веб проекта'''

from database import (Base, User, Post, SessionLocal, engine)
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()
app.mount("/static", StaticFiles(directory="public", html=True))

class UserModel(BaseModel):
    '''Модель для пользователя'''
    username: str
    email: str
    password: str

class PostModel(BaseModel):
    '''Модель для поста'''
    title: str
    content: str
    user_id: int

Base.metadata.create_all(bind=engine)

def get_db():
    """Получение сессии базы данных."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """Корневой маршрут для отображения index.html."""
    return FileResponse("public/index.html")

@app.get("/favicon.ico")
def favicon():
    '''Отображение иконки сайта (чтобы не выкидывал неудачное обращение в консоль)'''
    return FileResponse("public/favicon.ico")

@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    """Получение списка всех пользователей."""
    users = db.query(User).all()
    if not users:
        return {"status": "error", "message": "Пользователи не найдены"}
    return {"status": "success", "users": users}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Получение данных одного пользователя."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"status": "error", "message": f"Пользователь с ID {user_id} не найден"}
    return {"status": "success", "user": user}

@app.post("/users/")
def create_user(user: UserModel, db: Session = Depends(get_db)):
    """Добавление нового пользователя."""
    if db.query(User).filter(
        or_(User.username == user.username, User.email == user.email)).first():
        return {"status": "error", "message": "Пользователь с такими данными уже есть"}
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"status": "success", "user": db_user}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UserModel, db: Session = Depends(get_db)):
    """Обновление данных пользователя."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"status": "error", "message": f"Пользователь с ID {user_id} не найден"}
    if db.query(User).filter(
        and_(
            or_(User.username == updated_user.username, User.email == updated_user.email),
            User.id != user_id
        )
    ).first():
        return {"status": "error", "message": "Введённые данные не уникальны"}
    user.username = updated_user.username
    user.email = updated_user.email
    user.password = updated_user.password
    db.commit()
    db.refresh(user)
    return {"status": "success", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Удаление пользователя."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"status": "error", "message": f"Пользователь с ID {user_id} не найден"}
    db.query(Post).filter(Post.user_id == user_id).delete()
    db.delete(user)
    db.commit()
    return {"status": "success", "message": f"Пользователь с ID {user_id} удалён"}

@app.get("/posts/")
def get_all_posts(db: Session = Depends(get_db)):
    """Получение всех постов."""
    posts = db.query(Post).all()
    if not posts:
        return {"status": "error", "message": "Посты не найдены", "posts": []}
    return {"status": "success", "posts": posts}

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    """Получение одного поста."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {"status": "error", "message": f"Пост с ID {post_id} не найден"}
    return {"status": "success", "post": post}

@app.post("/posts/")
def create_post(post: PostModel, db: Session = Depends(get_db)):
    """Добавление нового поста."""
    if not db.query(User).filter(User.id == post.user_id).first():
        return {"status": "error", "message": f"Юзер с ID {post.user_id} не найден"}
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return {"status": "success", "post": db_post}

@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: PostModel, db: Session = Depends(get_db)):
    """Обновление поста."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {"status": "error", "message": f"Пост с ID {post_id} не найден"}
    if not db.query(User).filter(User.id == updated_post.user_id).first():
        return {"status": "error", "message": f"Юзер с ID {updated_post.user_id} не найден"}
    post.title = updated_post.title
    post.content = updated_post.content
    post.user_id = updated_post.user_id
    db.commit()
    db.refresh(post)
    return {"status": "success", "post": post}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """Удаление поста."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {"status": "error", "message": f"Пост с ID {post_id} не найден"}
    db.delete(post)
    db.commit()
    return {"status": "success", "message": f"Пост с ID {post_id} удалён"}
