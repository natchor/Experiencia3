from distutils.command.upload import upload
from django.db import models
from statistics import correlation


# Create your models here.
class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name='Id Comuna')
    nombreComuna=models.CharField(max_length=30, verbose_name='Nombre Comuna')

    def __str__(self): 
        return self.nombreComuna
        
class Cliente (models.Model): 
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre= models.CharField(max_length=20, verbose_name='Nombre')
    apellidos= models.CharField(max_length=30, verbose_name='Apellidos')
    correo= models.EmailField(max_length=20, verbose_name='Correo')
    password= models.CharField(max_length=8, verbose_name='Contrasena')
    fono= models.IntegerField( verbose_name='Fono')
    direccion= models.CharField(max_length=50, verbose_name='Direccion')
    comuna= models.ForeignKey(Comuna, on_delete=models.CASCADE)


    def __str__(self):
        return self.rut



class Productos(models.Model):
    idproducto = models.IntegerField(
        null=False, primary_key=True, verbose_name='id del producto')
    nombre = models.CharField(
        max_length=50, verbose_name='nombre del producto')
    imagen = models.ImageField(
        upload_to='img/', verbose_name="Imagen")
    description = models.TextField(null=True, verbose_name="Descripcion")
    cantidad = models.IntegerField(verbose_name='cantidad')
    precio = models.IntegerField(verbose_name='precio del producto')

    def __str__(self):
        return self.nombre


