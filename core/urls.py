from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicio/<int:pk>/', views.servicio_detalle, name='servicio_detalle'),
    path('reserva/<int:pk>/', views.realizar_reserva, name='realizar_reserva'),
]
