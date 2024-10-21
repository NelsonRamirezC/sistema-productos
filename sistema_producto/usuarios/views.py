from django.forms import ValidationError
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .forms import RegistroUsuarioForm

# Create your views here.

def index_view(request):
    return render(request, 'usuarios/usuarios.html', {})

def registro_view(request):
    
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            user = form.save() # recibimos al usuario para poder hacer uso de él, si es que queremos
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            HttpResponseRedirect("/")
        else:
            messages.error("Error al intentar registrar al usuario, por favor verifique los datos.")
                
    else:
        form = RegistroUsuarioForm()
        
        return render(request, 'usuarios/registro.html', {"form": form})


def login_view(request):
    return render(request, 'usuarios/login.html', {})
