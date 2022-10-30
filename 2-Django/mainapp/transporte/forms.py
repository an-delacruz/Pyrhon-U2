from tkinter import Widget
from django.forms import ModelForm,EmailInput,DateField
from transporte.models import Ciudad, Ruta, Chofer, Viaje
from django import forms
from django.contrib.admin import widgets
class CiudadForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Ciudad
        fields = '__all__'

class RutaForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Ruta
        fields = '__all__'

class ChoferForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Chofer
        fields = '__all__'

class ViajeForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Viaje
        fields = '__all__'