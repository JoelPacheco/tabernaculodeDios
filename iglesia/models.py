from django.db import models
# Create your models here.



class Ubigeo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    ubigeo = models.CharField(max_length=200)


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
    correoelectronico = models.EmailField(max_length=100)
    password = models.CharField(max_length=300)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    codigoubigeo = models.ForeignKey(Ubigeo)
    direccion = models.CharField(max_length=150)
    fechanacimiento = models.DateField()
    tipousuario = models.ForeignKey(TipoUsuario)
    tipodocumento = models.ForeignKey(TipoDocumento)
    fecharegistro = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now_add=True)
    estadousuario = models.BooleanField(default=True)
    sexo = models.CharField(max_length=2)
    estadocivil = models.CharField(max_length=2)
    admin = models.BooleanField(default=False)


