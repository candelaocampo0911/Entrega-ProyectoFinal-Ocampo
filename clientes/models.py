from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Clientes(models.Model): 
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    direccion = models.CharField(max_length=256)
    fecha_nacimiento= models.DateField()
    comentarios = models.TextField()

    def __str__(self):
        return f" {self.nombre} ,  {self.email} , {self.direccion} , {self.fecha_nacimiento} , {self.compra} , {self.comentarios} "



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





class Avatar(models.Model):
    # Va a estar asociado con el User. Avatar es una tabla anexa de User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"
    
