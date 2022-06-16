from rest_framework import serializers
from .models import Server
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class ServerForm(ModelForm):

    class Meta:
        model = Server
        fields = ['id', 'name', 'ip_address', 'description', 'server_is_active']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название сервера'
            }),
            "ip_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите IP (Пример: 0.0.0.0)'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'}),

            "server_is_active": CheckboxInput(attrs={
                'class': 'required checkbox'}),
        }