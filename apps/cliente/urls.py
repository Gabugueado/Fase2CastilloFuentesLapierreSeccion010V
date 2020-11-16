"""TiendaByjorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from apps.cliente.views import index, login_view,  tienda_list
# vistas basadas en funciones
from apps.cliente.views import contacto_view, listaUser_list, cliente_edit, cliente_delete
# vistas basadas en clases
from apps.cliente.views import RegistroUsuario, List, UserUpdate, UserDelete 
urlpatterns = [
    url('home', index, name='index'),
    url('contacto', contacto_view, name='contacto'),
    url('login', login_view, name='login'),
    url('tienda', tienda_list, name='tienda'),
    # vistas basadas en funciones
    # url('nuevo', cliente_view, name='cliente_crear'),
    # url('lista', listaUser_list, name='lista'),
    # url('editar/<int:pk>/', cliente_edit, name='cliente_editar'),
    # path('eliminar/<int:id_cliente>/', cliente_delete, name='cliente_eliminar'),
    # vistas basadas en clases
    url('registrar', RegistroUsuario.as_view(), name='registrar'),
    url('lista', List.as_view(), name='lista'),
    path('editar/<int:pk>/', UserUpdate.as_view(), name='cliente_editar'),
    path('eliminar/<pk>/', UserDelete.as_view(), name='cliente_eliminar')
]



