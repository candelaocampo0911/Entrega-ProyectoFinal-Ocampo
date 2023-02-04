from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from clientes.models import Avatar

from clientes.models import Clientes, Medio_pago, Articulos

class Clientesformulario(forms.Form):
    nombre=forms.CharField(max_length=128)
    email=forms.EmailField()
    direccion=forms.CharField(max_length=212)
    fecha_nacimiento=forms.DateField()
    comentarios=forms.Textarea()
    

class MedioPagoformulario(forms.Form): 
    medio_de_pago = forms.CharField(max_length=256)


class Articulosformulario(forms.Form): 
    codigo_de_articulo = forms.CharField(max_length=256)
    marca = forms.CharField(max_length=256)
    peso = forms.CharField(max_length=256)





class UserUpdateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ["last_name" , "first_name", "email"]


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar 
        fields = ['imagen']

