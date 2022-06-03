from django.shortcuts import render
from rest_framework import generics
from .serializer import ServerSerializer
from .models import Server

def main(request):
    return render(request, 'rbr_srv_side/index.html')

def about(request):
    return render(request, 'rbr_srv_side/about.html')

def page_not_found_view(request, exception):
    return render(request, 'rbr_srv_side/404.html', status=404)

def servers(request):
    servs = Server.objects.all()
    return render(request, 'rbr_srv_side/servers.html', {'title': 'Все сервера на сайте', 'server_info': servs})

def servers_add(request):
    servs = Server.objects.all()
    return render(request, 'rbr_srv_side/servers_add.html', {'title': 'Добавление сервера на сайт', 'server_info': servs})

def servers_status(request):
    servs = Server.objects.all()
    return render(request, 'rbr_srv_side/servers_status.html', {'title': 'Статус серверов', 'server_info': servs})
