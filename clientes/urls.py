from django.urls import path
from clientes import views
from clientes.views import *
from django.conf import Settings

urlpatterns = [
    path('Clientes/', listar_clientes, name='clientes'),
    path('Medio_pago/', listar_medio_pago, name='medio_pago'),
    path('Articulos/', listar_articulos, name='articulos'),
    path('Crear_clientes/', crear_clientes, name='crear_clientes'),
    path('Crear_medio_pago/', crear_medio_pago, name='crear_medio_pago'),
    path('Crear_articulos/', crear_articulos, name='crear_articulos'),
    path('Buscar_clientes/', buscar_clientes, name='buscar_clientes'),
    path ('' ,inicio , name='inicio'),


    path("clientes/" ,views.listar_clientes ,name="clientes"),
    path("medio_pago/",MedioPagoListView.as_view(), name="medio_pago"),
    path("articulo/",ArticulosListView.as_view(), name="articulos"),
    path("ver-clientes/<int:pk>/",ClientesDetailView.as_view(), name="ver_clientes"),
    path("ver-medio_pago/<int:pk>/",MedioPagoDetailView.as_view(), name="ver_medio_pago"),
    path("ver-articulo/<int:pk>/", ArticulosDetailView.as_view(), name="ver_articulos"),
    path("editar-clientes/<int:pk>/",ClientesUpdateView.as_view (), name="editar_clientes"),
    path("editar-medio_pago/<int:pk>/", MedioPagoUpdateView.as_view (), name="editar_medio_pago"),
    path("editar-articulos/<int:pk>/",ArticulosUpdateView.as_view (), name="editar_articulos"),
    path("eliminar-cliente/<int:pk>/",ClientesDeleteView.as_view (), name="eliminar_clientes"),
    path("eliminar-medio_pago/<int:pk>/",MedioPagoDeleteView.as_view (), name="eliminar_medio_pago"),
    path("eliminar-articulo/<int:pk>/",ArticulosDeleteView.as_view (), name="eliminar_articulos"),
    path("registro/",registro, name="registro"),
    path("login/",login_view, name="login"),
    path("logout/",CustomLogoutView.as_view(), name="logout"),
    #url perfil
    path("editar-perfil/",ProfileUpdateView.as_view(), name="editar_perfil"),
    path("agregar-avatar/",agregar_avatar, name="agregar_avatar"),


]

