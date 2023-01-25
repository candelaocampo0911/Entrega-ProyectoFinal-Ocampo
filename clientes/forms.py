from django import forms 

class Clientesformulario(forms.Form):
    nombre=forms.CharField(max_length=128)
    email=forms.EmailField()
    direccion=forms.CharField(max_length=212)
    fecha_nacimiento=forms.DateField()
    

class MedioPagoformulario(forms.Form): 
    medio_de_pago = forms.CharField(max_length=256)


class Articulosformulario(forms.Form): 
    codigo_de_articulo = forms.CharField(max_length=256)
    marca = forms.CharField(max_length=256)
    peso = forms.CharField(max_length=256)
