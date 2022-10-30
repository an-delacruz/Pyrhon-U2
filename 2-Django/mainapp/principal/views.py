from http.client import HTTPResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

# Create your views here.
def principal(request):
    #se abre el doc con la plantilla:
    plantillaExterna = open("C:/Users/Aduas/OneDrive/Desktop/PracticaDjango/mainapp/principal/template/principal.html")
    #cargar el doc de tipo template
    template = Template(plantillaExterna.read())
    #cerrar el doc externo
    plantillaExterna.close()
    #crear un contexto
    context = Context()
    documento = template.render(context)
    return HttpResponse(documento)