from django.contrib import admin
from .models import Avaliacao, Curso


# class detCurso(admin.ModelAdmin):
#     list_display = ('titulo', 'url', 'create', 'update', 'active')
#
#
# admin.site.register(Curso, detCurso)

@admin.register(Curso)
class detCurso(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'create', 'update', 'active')


@admin.register(Avaliacao)
class detAvaliacao(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'nota', 'comentarios', 'email', 'update')

# Register your models here.
