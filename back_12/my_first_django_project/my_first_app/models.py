'''Файл определения моделей'''

from django.db import models

class Author(models.Model):
    '''Модель автора'''
    name = models.CharField(max_length=15)
    birth_date = models.DateField()
    bio = models.TextField()

class AuthorDetails(models.Model):
    """Дополнительные данные об авторе (email, телефон)"""
    author = models.OneToOneField(Author, primary_key=True,
                                  on_delete=models.CASCADE, related_name='details')
    email = models.EmailField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

class Publisher(models.Model):
    """Модель издателя"""
    name = models.CharField(max_length=20)
    address = models.TextField()

class Genre(models.Model):
    """Модель жанра книги"""
    name = models.CharField(max_length=15)

class Book(models.Model):
    '''Модель книги'''
    title = models.CharField(max_length=20)
    publication_date = models.DateField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name='books',
                                  null=True, blank=True)
    genres = models.ManyToManyField(Genre)
