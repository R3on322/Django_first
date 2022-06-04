from django.urls import path
from .views import main, about
from .views import ServerViewSet as srv, ServerAddView as srv_add


urlpatterns = [
    path('servers/', srv.servers, name='servers'),
    path('servers/add', srv_add.servers_add, name='servers_add'),
    path('servers/add_post', srv_add.as_view()),
    path('servers/status', srv.servers_status, name='servers_status'),
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]