'''Маршруты приложения nested_app'''

from django.urls import path
from nested_app import views

urlpatterns = [
    path('', views.home, name='nested_app_home'),
    path('about', views.about, name='nested_app_about'),
    path('contact', views.contact, name='nested_app_contact'),
]
