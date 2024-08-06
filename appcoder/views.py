from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return HttpResponse("Vista de los estudiantes")

def profesores(request):
    return HttpResponse("Vista de los profesores")

def entregables(request):
    return HttpResponse("Vista de los entregables")