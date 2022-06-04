from rest_framework import generics
from django.shortcuts import render, redirect
from .serializer import ServerForm, ServerSerializer
from .models import Server

def main(request):
    return render(request, 'rbr_srv_side/index.html')

def about(request):
    return render(request, 'rbr_srv_side/about.html')

def page_not_found_view(request, exception):
    return render(request, 'rbr_srv_side/404.html', status=404)

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def servers_add(request):
        error = ''
        if request.method == 'POST':
            form = ServerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('servers')
            else:
                error = 'Неверный формат!'

        form = ServerForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'rbr_srv_side/servers_add.html', context)

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def servers(request):
        servs = Server.objects.all()
        return render(request, 'rbr_srv_side/servers.html', {'title': 'Все сервера на сайте', 'server_info': servs})

    def servers_status(request):
        servs = Server.objects.all()
        return render(request, 'rbr_srv_side/servers_status.html', {'title': 'Статус серверов', 'server_info': servs})

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer