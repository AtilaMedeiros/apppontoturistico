from django.contrib import admin
from .models import Comentarios
from .actions import reprova_comentarios, aprova_comentarios

# Register your models here.


class ComantarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovador']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentarios, ComantarioAdmin)
