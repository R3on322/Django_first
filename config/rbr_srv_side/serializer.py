from .models import Server
from django.forms import ModelForm, TextInput, Textarea



class ServerSerializer(ModelForm):

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
                'placeholder': 'Введите IP'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'})
        }