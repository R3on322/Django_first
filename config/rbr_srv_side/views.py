import django.db
from rest_framework import generics
from django.shortcuts import render, redirect
from .serializer import ServerForm
from .models import Server
from .chek_serv import chek_server_ip_name

def servers_add(request):
    error = ''
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servers')
        else:
            error = 'Ошибка ввода! Проверьте название сервера или IP адрес!'

    form = ServerForm()
    context = {
    'form': form,
    'error': error
    }
    return render(request, 'rbr_srv_side/servers_add.html', context)

def servers(request):
    servs = Server.objects.all()
    return render(request, 'rbr_srv_side/servers.html', {'title': 'Все сервера на сайте', 'server_info': servs})

def main(request):
    return render(request, 'rbr_srv_side/index.html')

def about(request):
    return render(request, 'rbr_srv_side/about.html')

def pageNotFound(request, exception):
    return render(request, 'rbr_srv_side/404.html', status=404)