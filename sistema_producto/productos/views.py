from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Producto

from django.contrib.auth.decorators import login_required, permission_required 


from .forms import ProductoForm

# Create your views here.

# VISTA PARA MOSTRAR TODOS LOS PRODUCTOS
def productos(request):
    
    #obtener todos los registros de la base de datos
    lista_productos = Producto.objects.all()
    
    contexto = {}
    contexto["productos"] = lista_productos
    
    return render(request, "productos/productos.html", contexto)



# VISTA PARA REGISTRAR NUEVOS PRODUCTOS
@login_required(login_url='/usuarios/login/')
@permission_required('productos.add_producto', raise_exception=False, login_url='/')
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
        
        
@login_required(login_url='/usuarios/login/')
@permission_required('productos.add_producto', raise_exception=False, login_url='/')
def add_producto_modelform(request):
    
    if request.method == 'POST':
        # LÓGICA PARA PROCESAR LOS DATOS Y GUARDARLOS
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            try:
                producto = form.save(commit=False)
                producto.clean() # váldamos que cumpla con las restricciones del modelo
                producto.save() # guardamos los datos del modelo
                messages.success(request, "producto creado correctamente.")
            
            except ValidationError as e:
                messages.error(request, e.messages)
        else:
            messages.error(request, "Error al intentar crear el producto, intente nuevamente.")
        
        return render(request, "productos/add_producto_modelform.html", {"form": ProductoForm()})
    
    else:
        form = ProductoForm()
        return render(request, "productos/add_producto_modelform.html", {"form": form})



@login_required(login_url='/usuarios/login/')
@permission_required('productos.productos_vip', raise_exception=False, login_url='/')
def productos_vip(request):
    return HttpResponse("acceso a productos vip")


@login_required(login_url='/usuarios/login/')
def productos_destacados(request):
    user = request.user
    print(user.get_all_permissions())
    return HttpResponse(f"Productos destacados, saludos {request.user.username}")


