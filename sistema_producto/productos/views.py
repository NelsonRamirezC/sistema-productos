from django.shortcuts import render
from .models import Producto

# Create your views here.

# VISTA PARA MOSTRAR TODOS LOS PRODUCTOS
def productos(request):
    
    #obtener todos los registros de la base de datos
    lista_productos = Producto.objects.all()
    
    contexto = {}
    contexto["productos"] = lista_productos
    
    return render(request, "productos/productos.html", contexto)



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
        
        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        
        if nuevo_producto:
            try:
                nuevo_producto.save()
                contexto = {
                    "producto": nuevo_producto,
                    "id": nuevo_producto.id,
                    "mensaje": "Producto creado correctamente"
                }
                return render(request, "productos/add_productos.html", contexto)
            except Exception as e:
                contexto = {
                "error": "Ha ocurrido un error al intentar conectarse con la base de datos."
            }
                
            return render(request, "productos/add_productos.html", contexto)
        else: 
            contexto = {
                "error": "No fue posible registrar el producto"
            }
            return render(request, "productos/add_productos.html", contexto)
        
        
        
def add_producto_modelform(request):
    if request.method == 'GET':
        return render(request, "productos/add_producto_modelform.html", {})
    
    if request.method == 'POST':
        # LÓGICA PARA PROCESAR LOS DATOS.
        
        
        return render(request, "productos/add_producto_modelform.html", {})

