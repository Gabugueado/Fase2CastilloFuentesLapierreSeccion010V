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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView
from apps.cliente.views import index, tienda_list, contacto_view, logout
# from apps.cliente.views import login_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/', include('apps.producto.urls')),
    path('cliente/',  include('apps.cliente.urls')),
    path('', index, name='index'),
    path('tienda', tienda_list, name='tienda'),
    path('contacto', contacto_view, name='contacto'),
    path('login/', LoginView.as_view(template_name='tienda/login.html'), name='login'),
    path('logout', logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social'))
]
