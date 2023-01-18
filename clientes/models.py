from django.db import models

# Create your models here.


class Clientes(models.Model): 
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    direccion = models.CharField(max_length=256)
    fecha_nacimiento= models.DateField()

    def __str__(self):
        return f" {self.nombre} ,  {self.email} , {self.direccion} , {self.fecha_nacimiento} , {self.compra}"



class Medio_pago(models.Model):
    medio_de_pago = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.medio_de_pago}"
    
    


class Articulos(models.Model): 
    codigo_de_articulo = models.CharField(max_length=256)
    marca = models.CharField(max_length=256)
    peso = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.codigo_del_producto} ,  {self.marca} ,  {self.peso} "



