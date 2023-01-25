from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from clientes.models import Clientes , Medio_pago , Articulos
from clientes.forms import Clientesformulario , Articulosformulario , MedioPagoformulario
from django.urls import reverse 


# Create your views here.


def inicio(request):
    return render(
        request=request,
        template_name='clientes/inicio.html',
    )




def listar_clientes(request):
    contexto = {
        'clientes' : Clientes.objects.all()
    }
    
    return render(
        request = request ,
        template_name = 'clientes/listar_clientes.html' ,
        context = contexto,
    )



def listar_medio_pago(request): 
    contexto = {
        'medio_pago' : Medio_pago.objects.all()
    }
    
    return render(
        request = request ,
        template_name = 'medio_pago/listar_medio_pago.html' ,
        context = contexto ,
    )



def listar_articulos(request): 
    contexto = {
        'articulos' : Articulos.objects.all()
    }
    
    return render(
        request = request ,
        template_name = 'articulos/listar_articulos.html' ,
        context = contexto ,
    )




def crear_clientes(request): 
    if request.method == "POST":
        formulario = Clientesformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Clientes(nombre=data['nombre'],
                            email=data['email'],
                            direccion=data['direccion'],
                            fecha_nacimiento=data['fecha_nacimiento'])
            
            cliente.save()
            creacion_exitosa = reverse('clientes')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = Clientesformulario()
    return render(
        request=request ,
        template_name = 'clientes/formularios_clientes.html' ,
        context={'formulario':formulario} ,
    )    



def crear_medio_pago(request): 
    if request.method == "POST":
        formulario = MedioPagoformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            medio_pago = Medio_pago(medio_de_pago=data["medio_de_pago"])
            
            medio_pago.save()
            creacion_exitosa = reverse('listar_medio_pago')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = MedioPagoformulario()
    return render(
        request=request ,
        template_name = 'medio_pago/crear_medio_pago.html' ,
        context={'formulario':formulario} ,
    )    



def crear_articulos(request): 
    if request.method == "POST":
        formulario = Articulosformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulos = Articulos(codigo_de_articulo=data['codigo_de_articulo'],
                            marca=data['marca'],
                            peso=data['peso'])
            
            articulos.save()
            creacion_exitosa = reverse('listar_articulos')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = Articulosformulario()
    return render(
        request=request ,
        template_name = 'articulos/crear_articulos.html' ,
        context={'formulario':formulario} ,
    )    




def buscar_clientes(request):
    if request.method == "POST": 
        data = request.POST
        clientes = Clientes.objects.filter(nombre__contains=data["nombre"])
        
        contexto= {
            'clientes' : clientes
        }
    return render(
        request=request ,
        template_name = 'clientes/buscar_clientes.html', 
        context=contexto , 
    )
