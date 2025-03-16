from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PedidoForm
from urllib.parse import quote_plus

from django.shortcuts import render

def home(request):
    
    beneficios = [
        {"titulo": "Experiencia y Profesionalismo", "descripcion": "Contamos con años de experiencia en mantenimiento de jardines y piscinas.", "icono": "bi bi-award"},
        {"titulo": "Materiales de Calidad", "descripcion": "Utilizamos herramientas y productos de alta calidad para garantizar los mejores resultados.", "icono": "bi bi-tools"},
        {"titulo": "Atención Personalizada", "descripcion": "Nos adaptamos a tus necesidades para ofrecerte el mejor servicio posible.", "icono": "bi bi-person-check"},
    ]
    
    servicios = [
        {"titulo": "Mantenimiento de Jardines", "descripcion": "Cuidamos y mantenemos tus áreas verdes con los mejores estándares.", "imagen": "mant_jar.jfif"},
        {"titulo": "Mantenimiento de Piscinas", "descripcion": "Limpieza y mantenimiento profesional para que tu piscina luzca impecable.", "imagen": "Limpieza_piscina.jfif"},
        {"titulo": "Poda de Árboles", "descripcion": "Corte y mantenimiento de árboles para mejorar su salud y estética.", "imagen": "poda_arboles.jfif"},
        {"titulo": "Corte de Césped", "descripcion": "Corte de césped profesional para mantener tu jardín siempre verde y bien cuidado.", "imagen": "corte_cesped.jfif"},
        {"titulo": "Poda de Arbustos", "descripcion": "Mantenemos tus arbustos saludables y bien formados con nuestra poda.", "imagen": "poda_arbustos.jfif"},
        {"titulo": "Sistemas de Riego", "descripcion": "Instalación y mantenimiento de sistemas de riego para un consumo eficiente.", "imagen": "sistema_riego.jfif"},
    ]
    
   
    
    
    return render(request, "pedidos/home.html", {"servicios": servicios, "beneficios": beneficios})


def pedido_view(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            direccion = form.cleaned_data['direccion']
            mensaje = form.cleaned_data['mensaje']
            
            # Crear el mensaje para enviar por WhatsApp
            body = f"Nuevo Pedido:\nNombre: {nombre}\nTeléfono: {telefono}\nDirección: {direccion}\nMensaje: {mensaje}"
            
            # Codificar el mensaje para URL
            mensaje_codificado = quote_plus(body)
            
            # Crear el enlace de WhatsApp
            whatsapp_url = f"https://wa.me/5491121674114?text={mensaje_codificado}"
            
            # Redirigir a la página de gracias con el whatsapp_url
            return render(request, 'pedidos/gracias.html', {'nombre': nombre, 'whatsapp_url': whatsapp_url})

    else:
        form = PedidoForm()

    return render(request, 'pedidos/pedido_form.html', {'form': form})

def gracias_view(request, nombre):
    # Obtener el enlace de WhatsApp de la solicitud GET
    whatsapp_url = request.GET.get('whatsapp_url', '')
    
    # Renderizar la plantilla 'gracias.html' con el nombre y el enlace de WhatsApp
    return render(request, 'pedidos/gracias.html', {'nombre': nombre, 'whatsapp_url': whatsapp_url})

def galeria(request):
    
    
    
    return render(request, 'pedidos/galeria.html', {'galeria': galeria  })