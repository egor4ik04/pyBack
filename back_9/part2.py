'''
    Остатки функций второй части заданий лабораторной работы. 
    Перенесены т.к. их форма меняется и часть остаётся висеть ненужной в конечном проекте.
'''

from database import (User, Post)
from sqlalchemy.orm import Session

def add_users(db: Session):
    """Добавляет пользователей в таблицу."""
    users = [
        User(username="Артур", email="artur@test.com", password="asasd123"),
        User(username="Иван", email="1van@test.com", password="1vangog"),
        User(username="Алексей", email="aleksey@test.com", password="alexa_test")
    ]
    db.add_all(users)
    db.commit()

def add_posts(db: Session):
    """Добавляет посты в таблицу, связывая их с пользователями."""
    users = db.query(User).all()
    posts = [
        Post(title="Мой первый пост", content="Привет мир! #первый", user_id=users[0].id),
        Post(title="Путешествия", content="Сегодня был в горах. Чистый воздух и природа.",
             user_id=users[1].id),
        Post(title="Мечты", content="Хочу посетить Японию и попробовать суши.",
             user_id=users[2].id),
        Post(title="Еда", content="Люблю пироги.", user_id=users[0].id),
        Post(title="Чтение", content="Начал читать новую книгу. Рекомендую всем!",
             user_id=users[1].id)
    ]
    db.add_all(posts)
    db.commit()

def get_all_users(db: Session):
    """Извлекает все записи пользователей из таблицы Users."""
    users = db.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, " +
              f"Email: {user.email}, Password: {user.password}")
    return users

def get_all_posts_with_users(db: Session):
    """Извлекает все посты с информацией о пользователях, которые их создали."""
    posts = db.query(Post).join(User).all()
    # Join соединяет Post и User по foreign key
    for post in posts:
        print(f"ID: {post.id}, Title: {post.title}, Content: {post.content}, " +
              f"UserId: {post.user_id}, Username: {post.user.username}")
    return posts

def get_posts_by_user(db: Session, user_id):
    """Извлекает все посты, связанные с конкретным пользователем по его ID."""
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    for post in posts:
        print(f"Title: {post.title}, Content: {post.content}")
    return posts

def update_user_email(db: Session, user_id, new_email):
    """Обновляет email пользователя по его ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        print(f"Email пользователя {user.username} обновлен на {new_email}")
    else:
        print(f"Пользователь с ID {user_id} не найден.")

def update_post_content(db: Session, post_id, new_content):
    """Обновляет content поста по его ID."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        db.commit()
        print(f"Content поста '{post.title}' обновлен.")
    else:
        print(f"Пост с ID {post_id} не найден.")

def delete_post(db: Session, post_id):
    """Удаляет пост по его ID."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        print(f"Пост с ID {post_id} удален.")
    else:
        print(f"Пост с ID {post_id} не найден.")

def delete_user(db: Session, user_id):
    """Удаляет пользователя и все его посты по его ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.query(Post).filter(Post.user_id == user_id).delete()
        db.delete(user)
        db.commit()
        print(f"Пользователь с ID {user_id} и все его посты удалены.")
    else:
        print(f"Пользователь с ID {user_id} не найден.")
