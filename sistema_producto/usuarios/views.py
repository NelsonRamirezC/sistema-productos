from django.forms import ValidationError
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import RegistroUsuarioForm, LoginUsuarioForm

# Create your views here.

def index_view(request):
    return render(request, 'usuarios/usuarios.html', {})

def registro_view(request):
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save() # recibimos al usuario para poder hacer uso de él, si es que queremos
            # login(request, user) -> definir si queremos que usuario quede logueado inmediatamente
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Error al intentar registrar al usuario, por favor verifique los datos.")
            return render(request, 'usuarios/registro.html', {"form": form})
                
    else:
        form = RegistroUsuarioForm()
        return render(request, 'usuarios/registro.html', {"form": form})


def login_view(request):
    form = None
    if request.method == 'POST':
        form = LoginUsuarioForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            print(email, password)
            
            try:
                user = User.objects.get(email=email)
                print(user)
                user = authenticate(username=user.username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Usuario {user.username} iniciado con éxito")
                    return HttpResponseRedirect("/")
                else:
                    messages.error(request, "Usuario o password incorrecto, verifique sus credenciales.")
                    return render(request, 'usuarios/login.html', {"form": form})
                
            except Exception as e:
                    print(e)
                    messages.error(request, "Usuario o password incorrecto, verifique sus credenciales.")
                    return render(request, 'usuarios/login.html', {"form": form})
        
        else:
            messages.error(request, "Usuario o contraseña inválidos, vuelva a intentar.")
            return render(request, 'usuarios/login.html', {"form": form})
    else: 
        
        form = LoginUsuarioForm()
        return render(request, 'usuarios/login.html', {"form": form})
    
    
    
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 
