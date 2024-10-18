from django.shortcuts import render
from .models import Producto

# Create your views here.

# VISTA PARA MOSTRAR TODOS LOS PRODUCTOS
def productos(request):
    return render(request, "productos/productos.html", {})

# VISTA PARA REGISTRAR NUEVOS PRODUCTOS
def add_productos(request):
    if request.method == 'GET':
        return render(request, "productos/add_productos.html", {})
    
    elif request.method == "POST":
        print("recibiendo datos mediante POST")
        
        #obtener datos deste el request nombre, descripcion, precio, stock
        
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        
        print(nombre, descripcion, precio, stock)
        
        nuevo_producto = Producto(nombre = nombre, descripcion=descripcion, precio=precio, stock = stock)
        
        if nuevo_producto:
            nuevo_producto.save()
            contexto = {
                "producto": nuevo_producto,
                "id": nuevo_producto.id,
                "mensaje": "Producto creado correctamente"
            }
            return render(request, "productos/add_productos.html", contexto)
        else: 
            contexto = {
                "error": "No fue posible registrar el producto"
            }
            return render(request, "productos/add_productos.html", contexto)

