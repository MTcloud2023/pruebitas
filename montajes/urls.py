"""
URL configuration for montajes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from monttools import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceso/',views.acceso, name = 'acceso'),
    path('registro/',views.registro, name = 'registro'),
    path('',views.principal, name = 'principal'),
    path('inicio/',views.inicio, name = 'inicio'),
    path('logout/',views.cerrarsesion, name = 'logout'),
    path('registro_data/',views.formulario, name = 'registrar data'),
    path('consulta_data/',views.consulta_datos, name='consulta'),
    path('detalle_data/', views.detalle, name = 'consulta a detalle'),
    path('detalle_data/<str:folio_id>', views.adetalle, name = 'consultaaespecifico'),


]
