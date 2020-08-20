from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovador = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username
