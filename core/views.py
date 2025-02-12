from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio, Reserva
from .forms import ReservaForm

# Vista para la página principal (mostrando todos los servicios)
def home(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/home.html', {'servicios': servicios})

# Vista para los detalles de un servicio
def servicio_detalle(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'core/servicio_detalle.html', {'servicio': servicio})

# Vista para realizar una reserva
def realizar_reserva(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.servicio = servicio
            reserva.save()
            return redirect('home')  # Redirige a la página principal después de hacer la reserva
    else:
        form = ReservaForm()

    return render(request, 'core/realizar_reserva.html', {'form': form, 'servicio': servicio})
