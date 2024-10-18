from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria']
        # fields = "__all__" -> incluir todos los atributos del modelo
        # exclude = ['direccion'] -> no incluir los atributos que queremos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'required': 'required', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'value': 9999999, 'min': 1}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'value': 0, 'min': 0}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }


        
        
        
        
    