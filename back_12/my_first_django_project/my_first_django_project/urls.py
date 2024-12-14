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

from django.urls import path
from my_first_app.views import extended_with_path, hello_world
from my_first_app.urls import HomeView, ExtendedView

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('home', HomeView.as_view(), name='home'),
    path('extended', ExtendedView.as_view(), name='extended'),
    path('extendedpath', extended_with_path, name='extended'),
]
