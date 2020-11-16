from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.producto.forms import ProductoForm
from apps.producto.models import Producto

# Create your views here.

def productos_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/producto/nuevo')
    else:
        form = ProductoForm()
    return render(request, 'tienda/registroProducto.html', {'form':form})

def listaProducto_list(request):
    producto =  Producto.objects.all()
    contexto = {'productos':producto}
    return render(request, 'tienda/listaCliente.html', contexto)