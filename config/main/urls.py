from django.urls import path
from .views import main, about
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]