from django.shortcuts import render
from rest_framework import generics


def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def pageNotFound(request, exception):
    return render(request, 'main/404.html', status=404)