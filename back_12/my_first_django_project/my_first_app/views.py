'''Уровень View приложения'''

from django.db.models import Count, Avg, Min, Max
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db import connection, DatabaseError, ProgrammingError
from .forms import AuthorForm, BookForm, PublisherForm, GenreForm, AuthorDetailsForm
from .models import Author, Book, Publisher, Genre, AuthorDetails

def execute_sql_query(request: HttpRequest):
    '''Выполнение произвольного SQL-запроса'''
    results = None
    columns = None
    message = None
    sql_query = request.POST.get('sql_query', '')
    if request.method == 'POST' and sql_query:
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                if sql_query.strip().lower().startswith('select'):
                    results = cursor.fetchall()
                    columns = [col[0] for col in cursor.description]
                else:
                    message = f"Запрос выполнен. Затронуто строк: {cursor.rowcount}."
        except (DatabaseError, ProgrammingError) as e:
            message = f"Ошибка выполнения SQL-запроса: {e}"
    return render(request, 'base.html', {
        'sql_query': sql_query,
        'results': results,
        'columns': columns,
        'message': message,
    })

def final_render(request: HttpRequest, template='base.html',
                 authors=None, books=None, publishers=None, genres=None, form=None, message='',
                 **kwargs):
    '''Финальное представление для заполнения различных данных'''
    authors = Author.objects.all() if authors is None else authors # pylint: disable=no-member
    books = Book.objects.all() if books is None else books # pylint: disable=no-member
    publishers = Publisher.objects.all() if publishers is None else publishers # pylint: disable=no-member
    genres = Genre.objects.all() if genres is None else genres # pylint: disable=no-member

    author_id = request.COOKIES.get('author_id')
    if author_id:
        authors, books = get_filtered_books_and_author(authors, books, author_id)
        publishers = []
        genres = []

    publisher_id = request.COOKIES.get('publisher_id')
    if publisher_id:
        publishers, books = get_filtered_books_and_publishers(publishers, books, publisher_id)
        authors = []
        genres = []

    genre_id = request.COOKIES.get('genre_id')
    if genre_id:
        genres, books = get_filtered_books_and_genres(genres, books, genre_id)
        authors = []
        publishers = []

    sort_order = request.COOKIES.get('sort_order')
    if sort_order:
        books = apply_sorting(books, sort_order)
        kwargs['current_sort_order'] = sort_order

    #books_values = books.values('title', 'publication_date', 'author__name')
    #filtered_kirillic = Book.objects.filter(publication_date__gte='1840-01-01') # pylint: disable=no-member
    #books_values = filtered_kirillic.values('title', 'publication_date', 'author__name')
    #books_values_list = books.values_list('title', 'publication_date', 'author__name')
    #books_values_list = books.intersection(filtered_kirillic).values_list(
    #    'title', 'publication_date', 'author__name')
    #kwargs['books_values'] = books_values
    #kwargs['books_values_list'] = books_values_list

    return render(request=request, template_name=template,
                  context={
                      'message': message,
                      'books': books,
                      'authors': authors,
                      'publishers': publishers,
                      'genres': genres,
                      'form': form,
                      **kwargs
                 })

def home(request: HttpRequest):
    '''Главная страница с обновлением данных'''
    if 'author_id' in request.COOKIES:
        del request.COOKIES['author_id']
    if 'publisher_id' in request.COOKIES:
        del request.COOKIES['publisher_id']
    if 'genre_id' in request.COOKIES:
        del request.COOKIES['genre_id']
    if 'sort_order' in request.COOKIES:
        del request.COOKIES['sort_order']
    response = final_render(request, message="Настройки сброшены.")
    response.delete_cookie('author_id')
    response.delete_cookie('publisher_id')
    response.delete_cookie('genre_id')
    response.delete_cookie('sort_order')
    return response


def get_authors(request: HttpRequest):
    '''Получение авторов'''
    return final_render(request)

def add_author(request: HttpRequest):
    '''Добавление нового автора'''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create( # pylint: disable=no-member
                name=form.cleaned_data['name'],
                birth_date=form.cleaned_data['birth_date'],
                bio=form.cleaned_data['bio']
            )
            return final_render(request, message='Автор успешно добавлен.')
    else:
        form = AuthorForm()
    return final_render(request, form=form)

def update_author(request: HttpRequest):
    '''Обновление информации об авторе'''
    author_id = request.GET.get('id')
    if not author_id:
        return final_render(request, message='ID автора не указан.')

    try:
        author = Author.objects.get(id=author_id)  # pylint: disable=no-member
    except Author.DoesNotExist:  # pylint: disable=no-member
        return final_render(request, message=f"Автор с ID {author_id} не найден.")

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return final_render(request, message=f"Автор с ID {author_id} был успешно обновлён.")
    else:
        form = AuthorForm(instance=author)
    return final_render(request, form=form)

def delete_author(request: HttpRequest):
    '''Удаление автора по ID'''
    author_id = request.GET.get('id')
    if not author_id:
        return final_render(request, message='ID автора не указан.')

    try:
        author = Author.objects.get(id=author_id)  # pylint: disable=no-member
        author.delete()
        return final_render(request, message=f"Автор с ID {author_id} был успешно удалён.")
    except Author.DoesNotExist:  # pylint: disable=no-member
        return final_render(request, message=f"Автор с ID {author_id} не найден.")


def author_details(request: HttpRequest):
    '''Страница для добавления и редактирования данных автора'''
    author_id = request.GET.get('author_id')
    if not author_id:
        return render(request, 'author_details.html', {'message': 'ID автора не указан'})
    try:
        author = Author.objects.get(id=author_id) # pylint: disable=no-member
    except Author.DoesNotExist: # pylint: disable=no-member
        return render(request, 'author_details.html', {'message': 'Автор не найден'})
    try:
        author_det = author.details
    except AuthorDetails.DoesNotExist: # pylint: disable=no-member
        author_det = None
    if request.method == 'POST':
        form = AuthorDetailsForm(request.POST, instance=author_det)
        if form.is_valid():
            author_det = form.save(commit=False)
            author_det.author = author
            form.save()
            return redirect('home')
    else:
        form = AuthorDetailsForm(instance=author_det)
    return render(request, 'author_details.html', {
        'form': form,
        'author': author,
        'author_details': author_det
    })

def delete_author_details(request: HttpRequest):
    '''Удаление дополнительных данных автора'''
    author_id = request.GET.get('author_id')
    try:
        author = Author.objects.get(id=author_id) # pylint: disable=no-member
    except Author.DoesNotExist: # pylint: disable=no-member
        return render(request, 'author_details.html', {'message': 'Автор не найден'})
    try:
        author_det = author.details
        author_det.delete()
        return redirect('home')
    except AuthorDetails.DoesNotExist: # pylint: disable=no-member
        return redirect('home')


def get_books(request: HttpRequest):
    '''Получение книг'''
    return final_render(request, message=None)

def add_book(request: HttpRequest):
    '''Добавление новой книги'''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                author_id = form.cleaned_data['author'].id
                author = Author.objects.get(id=author_id) # pylint: disable=no-member
            except Author.DoesNotExist: # pylint: disable=no-member
                return final_render(request, message=f"Автор с ID {author_id} не найден.")

            Book.objects.create( # pylint: disable=no-member
                title=form.cleaned_data['title'],
                publication_date=form.cleaned_data['publication_date'],
                author=author
            )
            return final_render(request, message='Книга успешно добавлена.')
    else:
        form = BookForm()
    return final_render(request, form=form)

def update_book(request: HttpRequest):
    '''Обновление информации о книге'''
    book_id = request.GET.get('id')
    if not book_id:
        return final_render(request, message='ID книги не указан.')

    try:
        book = Book.objects.get(id=book_id) # pylint: disable=no-member
    except Book.DoesNotExist: # pylint: disable=no-member
        return final_render(request, message=f"Книга с ID {book_id} не найдена.")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            author_id = form.cleaned_data['author'].id
            try:
                Author.objects.get(id=author_id) # pylint: disable=no-member
            except Author.DoesNotExist: # pylint: disable=no-member
                return final_render(request, message=f"Автор с ID {author_id} не найден.", form=form)
            form.save()
            return final_render(request, message=f"Книга с ID {book_id} была успешно обновлена.")
    else:
        form = BookForm(instance=book)
    return final_render(request, form=form)

def delete_book(request: HttpRequest):
    '''Удаление книги по ID'''
    book_id = request.GET.get('id')
    if not book_id:
        return final_render(request, message='ID книги не указан.')

    try:
        book = Book.objects.get(id=book_id)  # pylint: disable=no-member
        book.delete()
        return final_render(request, message=f"Книга с ID {book_id} была успешно удалена.")
    except Book.DoesNotExist:  # pylint: disable=no-member
        return final_render(request, message=f"Книга с ID {book_id} не найдена.")

def filter_books_by_author(request: HttpRequest):
    '''Установка фильтра по автору через куку'''
    author_id = request.GET.get('author_id')
    if not author_id:
        return final_render(request, message="ID автора для фильтрации не указан.")
    if 'publisher_id' in request.COOKIES:
        del request.COOKIES['publisher_id']
    if 'genre_id' in request.COOKIES:
        del request.COOKIES['genre_id']
    request.COOKIES['author_id'] = author_id
    response = final_render(request, message=f"Фильтр по автору с ID {author_id} установлен.")
    response.set_cookie('author_id', author_id)
    response.delete_cookie('publisher_id')
    response.delete_cookie('genre_id')
    return response

def filter_books_by_publisher(request: HttpRequest):
    '''Установка фильтра по издателю через куку'''
    publisher_id = request.GET.get('publisher_id')
    if not publisher_id:
        return final_render(request, message="ID издателя для фильтрации не указан.")
    if 'author_id' in request.COOKIES:
        del request.COOKIES['author_id']
    if 'genre_id' in request.COOKIES:
        del request.COOKIES['genre_id']
    request.COOKIES['publisher_id'] = publisher_id
    response = final_render(request, message=f"Фильтр по издателю с ID {publisher_id} установлен.")
    response.set_cookie('publisher_id', publisher_id)
    response.delete_cookie('author_id')
    response.delete_cookie('genre_id')
    return response

def filter_books_by_genre(request: HttpRequest):
    '''Установка фильтра по жанру через куку'''
    genre_id = request.GET.get('genre_id')
    if not genre_id:
        return final_render(request, message="ID жанра для фильтрации не указан.")
    if 'author_id' in request.COOKIES:
        del request.COOKIES['author_id']
    if 'publisher_id' in request.COOKIES:
        del request.COOKIES['publisher_id']
    request.COOKIES['genre_id'] = genre_id
    response = final_render(request, message=f"Фильтр по жанру с ID {genre_id} установлен.")
    response.set_cookie('genre_id', genre_id)
    response.delete_cookie('author_id')
    response.delete_cookie('publisher_id')
    return response

def get_filtered_books_and_author(authors, books, author_id):
    '''Фильтрация книг и получение автора по author_id'''
    try:
        author = authors.get(id=author_id) # pylint: disable=no-member
        filtered_books = books.filter(author=author) # pylint: disable=no-member
        return [author], filtered_books
    except Author.DoesNotExist: # pylint: disable=no-member
        return [], books.none()

def get_filtered_books_and_publishers(publishers, books, publisher_id):
    '''Фильтрация книг по издателю'''
    try:
        publisher = publishers.get(id=publisher_id) # pylint: disable=no-member
        filtered_books = books.filter(publisher=publisher) # pylint: disable=no-member
        return [publisher], filtered_books
    except Publisher.DoesNotExist: # pylint: disable=no-member
        return [], books.none()

def get_filtered_books_and_genres(genres, books, genre_id):
    '''Фильтрация книг по жанру'''
    try:
        genre = genres.get(id=genre_id) # pylint: disable=no-member
        filtered_books = books.filter(genres=genre) # pylint: disable=no-member
        return [genre], filtered_books
    except Publisher.DoesNotExist: # pylint: disable=no-member
        return [], books.none()

def set_sort_order(request: HttpRequest):
    '''Установка порядка сортировки книг через куку'''
    current_order = request.COOKIES.get('sort_order', 'asc')
    new_order = 'desc' if current_order == 'asc' else 'asc'
    request.COOKIES['sort_order'] = new_order
    response = final_render(request, message=f"Сортировка изменена на {new_order}.")
    response.set_cookie('sort_order', new_order)
    return response

def apply_sorting(books, sort_order):
    '''Применение сортировки к списку книг'''
    if sort_order == 'desc':
        return books.order_by('-publication_date')
    return books.order_by('publication_date')

def get_book_by_id(request: HttpRequest):
    '''Получение конкретной книги по ID'''
    book_id = request.GET.get('id')
    if not book_id:
        return render(request, 'base.html', {'message': 'ID книги не указан.'})
    try:
        book = Book.objects.get(id=book_id) # pylint: disable=no-member
        return render(request, 'base.html', {'book': book})
    except Book.DoesNotExist: # pylint: disable=no-member
        return render(request, 'base.html', {'message': f'Книга с ID {book_id} не найдена.'})

def books_aggregates(request: HttpRequest):
    '''Агрегатные операции над книгами'''
    aggregates = Book.objects.aggregate( # pylint: disable=no-member
        total_books=Count('id'),
        avg_book_id=Avg('id'),
        earliest_publication=Min('publication_date'),
        latest_publication=Max('publication_date')
    )
    return render(request, 'base.html', {
        'aggregates': aggregates
    })


def get_publishers(request: HttpRequest):
    '''Получение списка всех издателей'''
    return final_render(request, message="Список всех издателей.")

def add_publisher(request: HttpRequest):
    '''Добавление нового издателя'''
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return final_render(request, message="Издатель успешно добавлен.")
    else:
        form = PublisherForm()
    return final_render(request, form=form)

def update_publisher(request: HttpRequest):
    '''Редактирование информации об издателе'''
    publisher_id = request.GET.get('id')
    if not publisher_id:
        return final_render(request, message="ID издателя не указан.")
    try:
        publisher = Publisher.objects.get(id=publisher_id) # pylint: disable=no-member
    except Publisher.DoesNotExist: # pylint: disable=no-member
        return final_render(request, message=f"Издатель с ID {publisher_id} не найден.")
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return final_render(request, message=f"Издатель с ID {publisher_id} успешно обновлён.")
    else:
        form = PublisherForm(instance=publisher)
    return final_render(request, form=form)

def delete_publisher(request: HttpRequest):
    '''Удаление издателя'''
    publisher_id = request.GET.get('id')
    if not publisher_id:
        return final_render(request, message="ID издателя не указан.")
    try:
        publisher = Publisher.objects.get(id=publisher_id) # pylint: disable=no-member
        publisher.delete() # Удаляем издателя
        return final_render(request, message=f"Издатель с ID {publisher_id} успешно удалён.")
    except Publisher.DoesNotExist: # pylint: disable=no-member
        return final_render(request, message=f"Издатель с ID {publisher_id} не найден.")


def get_genres(request: HttpRequest):
    """Получение списка всех жанров"""
    return final_render(request, message="Список всех жанров.")

def add_genre(request: HttpRequest):
    """Добавление нового жанра"""
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return final_render(request, message="Жанр успешно добавлен.")
    else:
        form = GenreForm()
    return final_render(request, form=form)

def update_genre(request: HttpRequest):
    """Редактирование жанра"""
    genre_id = request.GET.get('id')
    if not genre_id:
        return final_render(request, message="ID жанра не указан.")
    try:
        genre = Genre.objects.get(id=genre_id) # pylint: disable=no-member
    except Genre.DoesNotExist: # pylint: disable=no-member
        return final_render(request, message=f"Жанр с ID {genre_id} не найден.")
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return final_render(request, message=f"Жанр с ID {genre_id} успешно обновлён.")
    else:
        form = GenreForm(instance=genre)
    return final_render(request, form=form)

def delete_genre(request: HttpRequest):
    """Удаление жанра"""
    genre_id = request.GET.get('id')
    if not genre_id:
        return final_render(request, message="ID жанра не указан.")
    try:
        genre = Genre.objects.get(id=genre_id) # pylint: disable=no-member
        genre.delete()
        return final_render(request, message=f"Жанр с ID {genre_id} успешно удалён.")
    except Genre.DoesNotExist: # pylint: disable=no-member
        return final_render(request, message=f"Жанр с ID {genre_id} не найден.")
