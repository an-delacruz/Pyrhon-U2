"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from principal.views import principal
from transporte.views import ciudad, detalleciudad, editarciudad, agregarciudad, eliminarciudad, chofer, detallechofer, editarchofer, agregarchofer, eliminarchofer
from transporte.views import ruta, detalleruta, editarruta, agregarruta, eliminarruta, viaje, detalleviaje, editarviaje, agregarviaje, eliminarviaje

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal, name='index'),
    path('ciudad/',ciudad,name='ciudad'),
    path('ciudad/detalle_ciudad/<int:id>', detalleciudad),
    path('ciudad/agregar_ciudad', agregarciudad),
    path('ciudad/editar_ciudad/<int:id>', editarciudad),
    path('ciudad/eliminar_ciudad/<int:id>',eliminarciudad),
    path('chofer/',chofer,name='chofer'),
    path('chofer/detalle_chofer/<int:id>', detallechofer),
    path('chofer/agregar_chofer', agregarchofer),
    path('chofer/editar_chofer/<int:id>', editarchofer),
    path('chofer/eliminar_chofer/<int:id>',eliminarchofer),
    path('ruta/',ruta,name='ruta'),
    path('ruta/detalle_ruta/<int:id>', detalleruta),
    path('ruta/agregar_ruta', agregarruta),
    path('ruta/editar_ruta/<int:id>', editarruta),
    path('ruta/eliminar_ruta/<int:id>',eliminarruta),
    path('viaje/',viaje, name='viaje'),
    path('viaje/detalle_viaje/<int:id>', detalleviaje),
    path('viaje/agregar_viaje', agregarviaje),
    path('viaje/editar_viaje/<int:id>', editarviaje),
    path('viaje/eliminar_viaje/<int:id>',eliminarviaje)
]
