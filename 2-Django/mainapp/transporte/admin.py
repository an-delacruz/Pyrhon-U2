from django.contrib import admin
from transporte.models import Ciudad, Chofer, Ruta, Viaje

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Chofer)
admin.site.register(Ruta)
admin.site.register(Viaje)
