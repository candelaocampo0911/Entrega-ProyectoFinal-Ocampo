from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from clientes.models import Clientes
from clientes.forms import RegistroUsuario
from django.urls import reverse 


# Create your views here.


def inicio(request):
    return render(
        request=request,
        template_name='users/home.html',
    )



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



def crear_clientes(request): 
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Clientes(nombre=data['nombre'],
                            email=data['email'],
                            direccion=data['direccion'],
                            fecha_de_nacimiento=data['fecha_de_nacimiento'])
            
            cliente.save()
            creacion_exitosa = reverse('listar_clientes')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = ClienteFormulario()
    return render(
        request=request ,
        template_name = 'clientes/crear_clientes.html' ,
        context={'formulario':formulario} ,
    )    



def buscar_cliente(request):
    if request.method == "POST": 
        data = request.POST
        clientes = Clientes.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__exact=data['busqueda'])
            )
        
        contexto= {
            'clientes' : clientes
        }
    return render(
        request=request ,
        template_name = 'clientes/buscar_clientes.html', 
        context=contexto , 
    )
