from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField(default=9999999)
    stock = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    