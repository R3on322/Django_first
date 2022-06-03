from django.shortcuts import render
from rest_framework import generics
from .serializer import ServerSerializer, ServerShortSerializer
from .models import Server
from django.http import HttpResponse

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerShortViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerShortSerializer

def main(request):
    return render(request, 'rbr_srv_side/index.html')

def about(request):
    return render(request, 'rbr_srv_side/about.html')


def page_not_found_view(request, exception):
    return render(request, 'rbr_srv_side/404.html', status=404)
