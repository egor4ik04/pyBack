'''Уровень View приложения'''

from django.http import HttpRequest
from django.shortcuts import render

def hello_world(request: HttpRequest):
    """render test"""
    group = "Unusual"
    names = request.GET.getlist("names")
    #names = ["Zero", "Adept_N", "Tester"]
    data = {"group": group, "names": names}
    return render(request, 'base.html', context=data)

def extended_with_path(request: HttpRequest):
    '''передаёт path в шаблон'''
    return render(request, 'extended.html',
                  {'path': request.get_full_path()})
