'''Шаблоны Django Forms'''

from django import forms
from .models import Author, Book, Publisher, Genre, AuthorDetails

class AuthorForm(forms.ModelForm):
    '''Форма для создания и редактирования автора'''
    class Meta:
        '''Метаданные автора'''
        model = Author
        fields = ['name', 'birth_date', 'bio']

class AuthorDetailsForm(forms.ModelForm):
    '''Форма для добавления и редактирования данных автора (email, телефон)'''
    class Meta:
        '''Метаданные доп. инфы автора'''
        model = AuthorDetails
        fields = ['email', 'phone']

class BookForm(forms.ModelForm):
    '''Форма для создания и редактирования автора'''
    class Meta:
        '''Метаданные книги'''
        model = Book
        fields = ['title', 'publication_date', 'author', 'publisher', 'genres']
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(), # pylint: disable=no-member
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class PublisherForm(forms.ModelForm):
    '''Форма для создания и редактирования издателя'''
    class Meta:
        '''Метаданные формы'''
        model = Publisher
        fields = ['name', 'address']

class GenreForm(forms.ModelForm):
    '''Форма для создания и редактирования жанра'''
    class Meta:
        '''Метаданные формы'''
        model = Genre
        fields = ['name']

class AuthorFormOld(forms.Form):
    '''Форма для создания и редактирования авторов'''
    name = forms.CharField(min_length=2, max_length=15, label="Имя автора")
    birth_date = forms.DateField(label="Дата рождения",
                                 widget=forms.DateInput(attrs={'type': 'date'}))
    bio = forms.CharField(widget=forms.Textarea, min_length=10,
                          max_length=500, label="Биография")

class BookFormOld(forms.Form):
    '''Форма для создания и редактирования книг'''
    title = forms.CharField(min_length=2, max_length=20, label="Название книги")
    publication_date = forms.DateField(label="Дата публикации",
                                       widget=forms.DateInput(attrs={'type': 'date'}))
    author = forms.IntegerField(label="ID автора")
