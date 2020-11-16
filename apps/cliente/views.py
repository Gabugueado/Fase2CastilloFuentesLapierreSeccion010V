from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# from apps.cliente.forms import ClienteForm
from apps.cliente.forms import RegistroForm
from apps.producto.models import Producto

# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def contacto_view(request):
    return render(request, 'tienda/contacto.html')

def login_view(request):
    return render(request, 'tienda/login.html')

def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/nuevo')
    else:
        form = ClienteForm()
    
    contexto = {'form':form}
    return render(request, 'tienda/registroCliente.html',contexto)

def cliente_edit(request, id_cliente):
    usuario = User.objects.get(id=id_cliente)
    if request.method == 'GET':
        form = RegistroForm(instance=usuario)
    else:
        form = RegistroForm(request.POST, instance=usuario)
        form.save()
        return redirect('/lista')
    return render(request, 'tienda/registroCliente.html')

def cliente_delete(request, id_cliente):
    usuario = User.objects.get(id=id_cliente)
    if request.method == 'POST':
        usuario.delete()
        return redirect('/lista')
    return render(request, 'tienda/Eliminar.html', {'usuario':usuario})


def listaUser_list(request):
    user = User.objects.all()
    contexto = {'users': user}
    return render(request, 'tienda/lista.html', contexto)

def tienda_list(request):
    producto =  Producto.objects.all()
    contexto = {'productos':producto}
    return render(request, 'tienda/tienda.html', contexto)

class RegistroUsuario(CreateView):
    model = User
    template_name = "tienda/registroCliente.html"
    form_class = RegistroForm
    success_url = reverse_lazy('registrar')

class List(ListView):
    model = User
    template_name = "tienda/lista.html"

class UserUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = "tienda/registroCliente.html"
    success_url = reverse_lazy('index')

class UserDelete(DeleteView):
    model = User
    template_name = "tienda/Eliminar.html"
    success_url = reverse_lazy('lista')

