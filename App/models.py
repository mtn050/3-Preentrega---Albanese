from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    contraseña=models.IntegerField()


class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    profesion=models.CharField(max_length=50)


class Compra(models.Model):
    nombre_cliente=models.CharField(max_length=50)
    dinero_Gastado=models.IntegerField()
    buen_cliente=models.BooleanField()

            