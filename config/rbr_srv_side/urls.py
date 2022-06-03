from django.urls import path
from .views import main, about, servers, servers_add, servers_status


urlpatterns = [
    path('servers/', servers, name='servers'),
    path('servers/add', servers_add, name='servers_add'),
    path('servers/status', servers_status, name='servers_status'),
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]