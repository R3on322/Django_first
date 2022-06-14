from django.urls import path
from .views import main, about
from .views import servers as all_servs, servers_add as add_servs
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/servers/', all_servs, name='servers'),
    path('api/servers/add', csrf_exempt(add_servs), name='servers_add'),
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]