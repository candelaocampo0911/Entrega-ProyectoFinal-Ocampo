from django.urls import path
from .views import *


urlpatterns = [
    path('Clientes/', listar_clientes, name='clientes'),
    path('Medio_pago/', listar_medio_pago, name='medio_pago'),
    path('Articulos/', listar_articulos, name='articulos'),
    path('Crear_clientes/', crear_clientes, name='crear_clientes'),
    path('Crear_medio_pago/', crear_medio_pago, name='crear_medio_pago'),
    path('Crear_articulos/', crear_articulos, name='crear_articulos'),
    path('Buscar_clientes/', buscar_clientes, name='buscar_clientes'),
    path ('' ,inicio , name='inicio'),
        
]
