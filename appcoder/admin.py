from django.contrib import admin

from .models import Curso, Estudiante, Profesor, Entregable
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")
    list_filter = ("nombre","comision")
    ordering = ("nombre","comision")

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
