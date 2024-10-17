from django.shortcuts import render

# Create your views here.

# VISTA PARA MOSTRAR TODOS LOS PRODUCTOS
def productos(request):
    return render(request, "productos/productos.html", {})

# VISTA PARA REGISTRAR NUEVOS PRODUCTOS
def add_productos(request):
    return render(request, "productos/add_productos.html", {})

