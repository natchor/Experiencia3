from statistics import correlation
from django.db import models

# Create your models here.
class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name='Id Comuna')
    nombreComuna=models.CharField(max_length=30, verbose_name='Nombre Comuna')

    def __str__(self): 
        return self.nombreComuna



class Cliente (models.Model): 
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    apellidos= models.CharField(max_length=20, verbose_name='Apellidos')
    correo= models.EmailField(max_length=20, verbose_name='Correo')
    password= models.CharField(max_length=8, verbose_name='Contrasena')
    fono= models.IntegerField( verbose_name='Fono')
    direccion= models.CharField(max_length=50, verbose_name='Direccion')
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name='Comuna')
    def __str__(self):
        return self.rut