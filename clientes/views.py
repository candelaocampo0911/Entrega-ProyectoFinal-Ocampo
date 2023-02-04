from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from clientes.models import Clientes , Medio_pago , Articulos , Avatar
from clientes.forms import Clientesformulario , Articulosformulario , MedioPagoformulario , UserUpdateForm, UserRegisterForm, AvatarFormulario
from django.urls import reverse, reverse_lazy 

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def inicio(request):
    return render(
        request=request,
        template_name='clientes/inicio.html',
    )

def about(request):
    contexto= {"about": about}
    return render(
        request=request,
        template_name="clientes/about.html"
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
        template_name = 'clientes/listar_medio_pago.html' ,
        context = contexto ,
    )



def listar_articulos(request): 
    contexto = {
        'articulos' : Articulos.objects.all()
    }
    
    return render(
        request = request ,
        template_name = 'clientes/listar_articulos.html' ,
        context = contexto ,
    )



@login_required
def crear_clientes(request): 
    if request.method == "POST":
        formulario = Clientesformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Clientes(nombre=data['nombre'],
                            email=data['email'],
                            direccion=data['direccion'],
                            fecha_nacimiento=data['fecha_nacimiento'],
                            )
            
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


@login_required
def crear_medio_pago(request): 
    if request.method == "POST":
        formulario = MedioPagoformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            medio_pago = Medio_pago(medio_de_pago=data["medio_de_pago"])
            
            medio_pago.save()
            creacion_exitosa = reverse('medio_pago')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = MedioPagoformulario()
    return render(
        request=request ,
        template_name = 'clientes/formularios_medio_pago.html' ,
        context={'formulario':formulario} ,
    )    


@login_required
def crear_articulos(request): 
    if request.method == "POST":
        formulario = Articulosformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulos = Articulos(codigo_del_articulo=data['codigo_del_articulo'],
                            marca=data['marca'],
                            peso=data['peso'])
            
            articulos.save()
            creacion_exitosa = reverse('articulos')
            return redirect(creacion_exitosa)
        
    else: #GET
        formulario = Articulosformulario()
    return render(
        request=request ,
        template_name = 'clientes/formularios_articulos.html' ,
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






class ClientesListView(ListView):
    model = Clientes
    template_name = "clientes/listar_clientes.html"


class MedioPagoListView(ListView):
    model = Medio_pago
    template_name = "clientes/listar_medio_pago.html"


class ArticulosListView(ListView):
    model = Articulos
    template_name = "clientes/listar_articulos.html"



class ClientesDetailView(DetailView):
    model = Clientes
    success_url = reverse_lazy ('clientes')
    template_name = "clientes/detalle_clientes.html"


class MedioPagoDetailView(DetailView):
    model = Medio_pago
    success_url = reverse_lazy ('medio_pago')
    template_name = "clientes/detalle_medio_pago.html"

class ArticulosDetailView(DetailView):
    model = Articulos
    success_url = reverse_lazy ('articulos')
    template_name = "clientes/detalle_articulos.html"


class ClientesUpdateView(LoginRequiredMixin,UpdateView):
    model = Clientes
    fields = ['nombre', 'email', 'direccion', "fecha_nacimiento" ]
    success_url = reverse_lazy('clientes')
    template_name = "clientes/clientes_form.html"

class MedioPagoUpdateView(LoginRequiredMixin,UpdateView):
    model = Medio_pago
    fields = ['medio_de_pago']
    success_url = reverse_lazy('medio_pago')
    template_name = "clientes/medio_pago_form.html"

class ArticulosUpdateView(LoginRequiredMixin,UpdateView):
    model = Articulos
    fields = ['codigo_de_articulo', 'marca', 'peso']
    success_url = reverse_lazy ("articulos")
    template_name = "clientes/articulos_form.html"




class ClientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes')
    template_name = "clientes/confirmar_eliminacion_clientes.html"


class MedioPagoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medio_pago
    success_url = reverse_lazy('medio_pago')
    template_name = "clientes/confirmar_eliminacion_medio_pago.html"

class ArticulosDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulos
    success_url = reverse_lazy('articulos')
    template_name = "clientes/confirmar_eliminacion_articulos.html"






def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='clientes/registro.html',
        context={'form': formulario},
    )



def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='clientes/login.html',
        context={'form': form},
    )







class CustomLogoutView(LogoutView):
    template_name = 'clientes/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'clientes/perfil_formulario.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='clientes/avatar_formulario.html',
        context={'form': formulario},

    )
    



