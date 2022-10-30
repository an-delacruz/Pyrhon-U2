from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Ciudad {self.id}: {self.nombreCiudad}'

class Chofer(models.Model):
    nombreChofer = models.CharField(max_length=255)
    domicilioChofer = models.CharField(max_length=255)
    edadChofer = models.IntegerField()
    ciudadNacimiento = models.ForeignKey(Ciudad,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Chofer {self.id}: {self.nombreChofer}'

class Ruta(models.Model):
    nombreRuta = models.CharField(max_length=255)
    distanciaRuta = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self) -> str:
        return f'Ruta {self.id}: {self.nombreRuta}'

class Viaje(models.Model):
    ruta = models.ForeignKey(Ruta,on_delete=models.SET_NULL,null=True)
    chofer = models.ForeignKey(Chofer,on_delete=models.SET_NULL,null=True)
    fechaViaje = models.DateField()
    observaciones = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Viaje {self.id}: {self.ruta}, chofer {self.chofer}, fechaViaje {self.fechaViaje}'

