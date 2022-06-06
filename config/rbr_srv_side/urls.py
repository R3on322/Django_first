from django.urls import path
from .views import main, about
from .views import ServerViewSet as srv, ServerAddView as srv_add


urlpatterns = [
    path('api/servers/', srv.servers, name='servers'),
    path('api/servers/add', srv_add.servers_add, name='servers_add'),
    path('api/servers/add_post', srv_add.as_view()),
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]