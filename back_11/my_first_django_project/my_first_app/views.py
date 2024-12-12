'''Уровень View приложения'''

from django.http import (
    JsonResponse,
    HttpResponse, HttpRequest, HttpResponseRedirect
    )
from django.shortcuts import redirect

def hello_world(request: HttpRequest):
    '''функция-представление, записывающая имя пользователя в куки'''
    username = request.GET.get("username")
    if username:
        response = HttpResponse(f"Имя {username} записано в куки")
        response.set_cookie("username", username)
        return response
    return HttpResponse("Имя не указано")

def show_cookies(request: HttpRequest):
    '''функция-представление, отображающая все куки'''
    return HttpResponse(request.COOKIES.items())

def hello_2(request: HttpRequest):
    '''функция-представление, приветствующая пользователя из данных строки запроса'''
    name = request.GET.get("name", "Empty")
    age = request.GET.get("age", 0)
    return HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>")

def temp_redirect_example(request: HttpRequest):
    '''Перенаправление на hello2 с параметрами по умолчанию'''
    return HttpResponseRedirect("hello2")

def redirect_example(request: HttpRequest):
    '''Перенаправление на hello2 через redirect'''
    return redirect('/hello2')

def json_example(request: HttpRequest):
    '''Представление, возвращающее json'''
    return JsonResponse({"name": "Tester", "age": 22})

# Замененённые и неиспользованные

def old_hello1(request: HttpRequest, name="Empty", age=0):
    '''функция-представление, приветствующая пользователя'''
    return HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>", status=302)

def old_hello_world(request: HttpRequest):
    '''Hello World изначальная функция'''
    return HttpResponse("<h1>Hello, World!</h1>")
