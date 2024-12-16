"""
URL configuration for my_first_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from my_first_app import views

authors_details_urls = [
    path('details', views.author_details, name='author_details'),
    path('details/delete', views.delete_author_details,
         name='delete_author_details'),
]

authors_urls = [
    path('get_all', views.get_authors, name='authors_list'),
    path('add', views.add_author, name='author_create'),
    path('edit', views.update_author, name='author_update'),
    path('delete', views.delete_author, name='author_delete'),
    path('details/', include(authors_details_urls)),
]

books_urls = [
    path('get_all', views.get_books, name='books_list'),
    path('add', views.add_book, name='book_create'),
    path('edit', views.update_book, name='book_update'),
    path('delete', views.delete_book, name='book_delete'),
    path('filter_aut', views.filter_books_by_author, name='filter_books_by_author'),
    path('filter_pub', views.filter_books_by_publisher, name='filter_books_by_publisher'),
    path('filter_gen', views.filter_books_by_genre, name='filter_books_by_genre'),
    path('sort', views.set_sort_order, name='set_sort_order'),
    path('aggregates', views.books_aggregates, name='books_aggregates'),
]

publishers_urls = [
    path('get_all', views.get_publishers, name='publishers_list'),
    path('add', views.add_publisher, name='publisher_add'),
    path('edit', views.update_book, name='publisher_update'),
    path('delete', views.delete_publisher, name='publisher_delete'),
]

genres_urls = [
    path('get_all', views.get_genres, name='genres_list'),
    path('add', views.add_genre, name='genre_add'),
    path('edit', views.update_genre, name='genre_update'),
    path('delete', views.delete_genre, name='genre_delete'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', include(authors_urls)),
    path('books/', include(books_urls)),
    path('book', views.get_book_by_id, name='get_book_by_id'),
    path('sql', views.execute_sql_query, name='execute_sql_query'),
    path('publishers/', include(publishers_urls)),
    path('genres/', include(genres_urls)),

]
