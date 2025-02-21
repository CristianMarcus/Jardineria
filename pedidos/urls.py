from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('galeria/', views.galeria, name='galeria'),  # Ruta para la galería de imágenes
    path('pedido/', views.pedido_view, name='pedido'),  # Ruta para el formulario de pedido
    path('gracias/<str:nombre>/', views.gracias_view, name='gracias'),  # Ruta para la página de gracias
]
