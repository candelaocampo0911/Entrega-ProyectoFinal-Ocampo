from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from clientes.models import Clientes
from clientes.forms import RegistroUsuario
from django.urls import reverse 


# Create your views here.

"""
def inicio(request):
    return render(
        request=request,
        template_name='users/home.html',
    )

"""

"""
def login(request):
    return render(
        request=request,
        template_name='users/login.html',
    )
"""



def listar_clientes(request):
    clientes = {
        'clientes' : Clientes.objects.all()
    }
    
    return render(
        request = request ,
        template_name = 'clientes/listar_clientes.html' ,
        context = clientes ,
    )


"""
def crear_clientes(request): 
    if request.method == "POST"
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Clientes(nombre=data['nombre'],
                            email=data['email'],
                            direccion=data['direccion'],
                            fecha_de_nacimiento=data['fecha_de_nacimiento'])
            
            cliente.save()
"""

"""
def registro_clientes(request):
        if request.method == "POST":
            
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Clientes(nombre=data['nombre'],
                            email=data['email'],
                            direccion=data['direccion'],
                            fecha_de_nacimiento=data['fecha_de_nacimiento'],


                            )

            cliente.save()
            url_exitosa = reverse('Articulos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = RegistroUsuario()
    return render(
        request=request,
        template_name='users/registro.html',
        context={'formulario': formulario},
    )

"""