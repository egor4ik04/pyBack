'''Уровень View приложения'''

from django.http import HttpResponse

def home(request):
    """Отображает главную страницу приложения nested_app."""
    return HttpResponse("nested_app. Главная страница")

def about(request):
    """Отображает страницу 'О нас' приложения nested_app."""
    return HttpResponse("nested_app. О нас")

def contact(request):
    """Отображает страницу 'Контакты' приложения nested_app."""
    return HttpResponse("nested_app. Контакты")
