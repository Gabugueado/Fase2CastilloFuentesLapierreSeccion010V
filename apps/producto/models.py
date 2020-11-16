from django.db import models

# from apps.proveedor.models import Proveedor

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    # fecha = models.DateField()
    # proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.descripcion, self.precio)


