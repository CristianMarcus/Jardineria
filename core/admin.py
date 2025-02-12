from django.contrib import admin
from .models import Servicio, Cliente, Reserva

# Registramos los modelos en el panel de administración
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Reserva)
