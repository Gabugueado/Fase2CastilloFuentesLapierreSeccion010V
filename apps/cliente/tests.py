from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from apps.producto.models import Producto

class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(nombre="pera", precio="1000")
        Producto.objects.create(nombre="manzana", precio="2000")

    def test_Producto_can_precio(self):
        """Productos that can precio are correctly identified"""
        pera = Producto.objects.get(nombre="pera")
        manzana = Producto.objects.get(nombre="manzana")
        Producto.objects.all()