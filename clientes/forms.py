from django import forms 

class RegistroUsuario(forms.Form):
    nombre=forms.CharField(max_length=128)
    email=forms.EmailField()
    direccion=forms.CharField(max_length=212)
    fecha_de_nacimiento=forms.DateField()
    
