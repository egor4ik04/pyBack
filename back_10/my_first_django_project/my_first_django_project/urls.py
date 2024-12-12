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

from django.urls import include, path#, re_path
from my_first_app import views

urlpatterns = [
    path('nested/', include('nested_app.urls')),
    path('hello', views.hello_world, name='hello_world'),
    path('cookie', views.show_cookies, name='show_cookies'),
    path('json', views.json_example, name='json_example'),
    path('redirect1', views.temp_redirect_example, name='temp_redirect_example'),
    path('redirect2', views.redirect_example, name='redirect_example'),
    path("hello2", views.hello_2),
    # re_path(r'^hello/(?P<name>\D+)/(?P<age>\d+)', views.hello_world, name='hello_world'),
    # re_path(r'^hello/(?P<name>\D+)', views.hello_world, name='hello_world'),
    # re_path(r'^hello', views.hello_world, name='hello_world'),
]
