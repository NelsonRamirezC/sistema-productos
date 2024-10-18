from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    precio = models.IntegerField(default=9999999, blank=False, null=False)
    stock = models.IntegerField(default=0, blank=False, null=False)
    estado = models.BooleanField(default=True, blank=False, null=False)
    categoria = models.CharField(default='Sin categoría', blank=False, null=False, max_length=50)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"
    