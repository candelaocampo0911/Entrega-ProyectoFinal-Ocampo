from django.urls import path
from clientes.views import inicio , registro , login


urlpatterns = [
    path('Registro/', registro, name='registro'),
    path('Login/', login, name='login'),          
]
