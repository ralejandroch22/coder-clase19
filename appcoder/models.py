from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30) ##Genera un string, con maximo de longitud
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30) ##Genera un string, con maximo de longitud
    apellido = models.CharField(max_length=30) ##Genera un string, con maximo de longitud
    email = models.EmailField() #Este modelo trae validaciones de email para guardar
    #nuevodato = model.charfield(null=True, blank=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()