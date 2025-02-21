from django import forms

class PedidoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'})
    )
    telefono = forms.CharField(
        max_length=15, 
        label="Teléfono", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1122334455'})
    )
    direccion = forms.CharField(
        label="Dirección", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ej: Calle 850, Localidad'})
    )
    mensaje = forms.CharField(
        label="Mensaje", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles Servicio...'})
    )
