from django.shortcuts import render, get_object_or_404, redirect #arrohas el error, si no existe persona
from transporte.models import Ciudad, Chofer, Ruta,Viaje
from transporte.forms import CiudadForm, ChoferForm, RutaForm, ViajeForm

# Create your views here.
#VIEWS DE CIUDAD INICIO
def ciudad(request):
        ciudad = Ciudad.objects.order_by('id')
        return render(request,'ciudad.html',{'Ciudad':ciudad})

def detalleciudad(request,id):
        ciudad = get_object_or_404(Ciudad, pk=id)
        return render(request,'detallesciudad.html',{'ciudad':ciudad})

def agregarciudad(request):
        if request.method=="POST":
                formaCiudad = CiudadForm(request.POST)
                if formaCiudad.is_valid():
                        formaCiudad.save()
                        return redirect('ciudad')
        else:
                formaCiudad = CiudadForm()
                return render(request, 'agregarciudad.html', {'formaCiudad':formaCiudad})

def editarciudad(request, id):
        ciudad = get_object_or_404(Ciudad, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaCiudad = CiudadForm(request.POST,instance=ciudad)#objeto que ya existe, y si existe cuales son los valores
                if formaCiudad.is_valid():
                        formaCiudad.save()
                        return redirect('ciudad')
        else:
                formaCiudad = CiudadForm(instance=ciudad)
                return render(request, 'editarciudad.html', {'formaCiudad':formaCiudad})

def eliminarciudad(request, id):
        ciudad = get_object_or_404(Ciudad, pk=id)#se busca nmediante el id
        if ciudad:
                ciudad.delete()
        return redirect('index')

#VIEW DE CIUDAD TERMINO

#VIEWS DE CHOFER INICIO

def chofer(request):
        chofer = Chofer.objects.order_by('id')
        return render(request,'chofer.html',{'Chofer':chofer})


def detallechofer(request,id):
        chofer = get_object_or_404(Chofer, pk=id)
        return render(request,'detalleschofer.html',{'chofer':chofer})

def agregarchofer(request):
        if request.method=="POST":
                formachofer = ChoferForm(request.POST)
                if formachofer.is_valid():
                        formachofer.save()
                        return redirect('chofer')
        else:
                formachofer = ChoferForm()
                return render(request, 'agregarchofer.html', {'formachofer':formachofer})

def editarchofer(request, id):
        chofer = get_object_or_404(Chofer, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formachofer = ChoferForm(request.POST,instance=chofer)#objeto que ya existe, y si existe cuales son los valores
                if formachofer.is_valid():
                        formachofer.save()
                        return redirect('chofer')
        else:
                formachofer = ChoferForm(instance=chofer)
                return render(request, 'editarchofer.html', {'formachofer':formachofer})

def eliminarchofer(request, id):
        chofer = get_object_or_404(Chofer, pk=id)#se busca nmediante el id
        if chofer:
                chofer.delete()
        return redirect('chofer')

#VIEWS DE CHOFER TERMINO

#VIEWS DE RUTA INICIO
def ruta(request):
        ruta = Ruta.objects.order_by('id')
        return render(request,'ruta.html',{'Ruta':ruta})

def detalleruta(request,id):
        ruta = get_object_or_404(Ruta, pk=id)
        return render(request,'detallesruta.html',{'ruta':ruta})

def agregarruta(request):
        if request.method=="POST":
                formaruta = RutaForm(request.POST)
                if formaruta.is_valid():
                        formaruta.save()
                        return redirect('ruta')
        else:
                formaruta = RutaForm()
                return render(request, 'agregarruta.html', {'formaruta':formaruta})

def editarruta(request, id):
        ruta = get_object_or_404(Ruta, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaruta = RutaForm(request.POST,instance=ruta)#objeto que ya existe, y si existe cuales son los valores
                if formaruta.is_valid():
                        formaruta.save()
                        return redirect('ruta')
        else:
                formaruta = RutaForm(instance=ruta)
                return render(request, 'editarruta.html', {'formaruta':formaruta})

def eliminarruta(request, id):
        ruta = get_object_or_404(Ruta, pk=id)#se busca nmediante el id
        if ruta:
                ruta.delete()
        return redirect('ruta')

#VIEWS DE RUTA TERMINO
def viaje(request):
        viaje = Viaje.objects.order_by('id')
        return render(request,'viaje.html',{'Viaje':viaje})

def detalleviaje(request,id):
        viaje = get_object_or_404(Viaje, pk=id)
        return render(request,'detallesviaje.html',{'viaje':viaje})

def agregarviaje(request):
        if request.method=="POST":
                formaviaje = ViajeForm(request.POST)
                if formaviaje.is_valid():
                        formaviaje.save()
                        return redirect('viaje')
        else:
                formaviaje = ViajeForm()
                return render(request, 'agregarviaje.html', {'formaviaje':formaviaje})

def editarviaje(request, id):
        viaje = get_object_or_404(Viaje, pk=id)#se busca nmediante el id
        if request.method=="POST":
                formaviaje = ViajeForm(request.POST,instance=viaje)#objeto que ya existe, y si existe cuales son los valores
                if formaviaje.is_valid():
                        formaviaje.save()
                        return redirect('viaje')
        else:
                formaviaje = ViajeForm(instance=viaje)
                return render(request, 'editarviaje.html', {'formaviaje':formaviaje})

def eliminarviaje(request, id):
        viaje = get_object_or_404(Viaje, pk=id)#se busca nmediante el id
        if viaje:
                viaje.delete()
        return redirect('viaje')
