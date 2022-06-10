from django.urls import path
from .views import main, about
from .views import ServerViewSet as srv, ServerAddView as srv_add
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/servers/', srv.servers, name='servers'),
    path('api/servers/add', csrf_exempt(srv_add.servers_add), name='servers_add'),
    path('api/servers/add_post', srv_add.as_view()),
    path('', main, name='main'),
    path('about', about, name='about_me'),
    ]