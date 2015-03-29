from django.db import models
from datetime import datetime
# Create your models here.

class Ubigeo(models.Model):
    id = models.AutoField(primary_key=True)
    codigodepartamento = models.CharField(max_length=2)
    codigoprovincia = models.CharField(max_length=2)
    codigodistrito = models.CharField(max_length=2)
    departamento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numerodocumento = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=15)
    ubigeo = models.ForeignKey(Ubigeo)
    direccion = models.CharField(max_length=150)
    fechanacimiento = models.DateField()
    tipousuario = models.ForeignKey(TipoUsuario)
    tipodocumento = models.ForeignKey(TipoDocumento)
    fecharegistro = models.DateTimeField(auto_now_add=True, blank=True)


