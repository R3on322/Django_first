from django.db import models

class Server(models.Model):

    name = models.CharField('name', max_length=255, unique=True)
    ip_address = models.GenericIPAddressField('IP', max_length=16, unique=True)
    description = models.TextField('description', default='no_description')
    server_is_active = models.BooleanField('is_active', default=False)

    def __str__(self):
        return self.name

    class Meta():
        managed = True
        verbose_name = 'Сервер'
        verbose_name_plural = 'Сервера'