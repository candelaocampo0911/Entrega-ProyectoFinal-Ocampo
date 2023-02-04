from django.contrib import admin


from clientes.models import Clientes , Medio_pago , Articulos

admin.site.register(Clientes)
admin.site.register(Medio_pago)
admin.site.register(Articulos)

#admin.site.registrer(Avatar)
