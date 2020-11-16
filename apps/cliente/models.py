from django.db import models

from apps.producto.models import Producto

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    direccion = models.TextField()
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)