from django.db import models
from django.forms import ValidationError

# Create your models here.

class Producto(models.Model):
    
    class Meta:
        permissions = (
            ('productos_vip', 'Puede visualizar exclusivos'),
        )
    
    CATEGORIAS = [
        ('HOGAR', 'Hogar'),
        ('COCINA', 'Cocina'),
        ('JARDIN', 'Jardín'),
        ('SIN_CATEGORIA', 'Sin categoría')
    ]
    
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    precio = models.PositiveIntegerField(default=9999999, blank=False, null=False)
    stock = models.PositiveIntegerField(default=0, blank=False, null=False)
    estado = models.BooleanField(default=True, blank=False, null=False)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='SIN_CATEGORIA')
    
    
    def clean(self):
        if self.precio <=0:
            raise ValidationError("El precio debe ser mayor que 0.")
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio}"
    