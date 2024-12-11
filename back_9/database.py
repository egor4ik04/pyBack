'''Модуль связи с БД. Первая часть заданий лабораторной работы.'''

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///C:/SQLite/databases/mytestdb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"check_same_thread": False})

class Base(DeclarativeBase): # pass
    """Базовый класс для моделей."""

class User(Base):
    """Модель таблицы Users."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    """Модель таблицы Posts."""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="posts")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
