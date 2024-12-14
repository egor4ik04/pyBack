"""
Template configuration for my_first_app.
"""

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    """Шаблон домашнего представления"""
    template_name = 'base.html'

class ExtendedView(TemplateView):
    """Шаблон расширенного base представления"""
    template_name = 'extended.html'
