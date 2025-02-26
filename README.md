# 🌿 Jardinería y Piscinas - Sistema de Pedidos Online

## 📌 Descripción del Proyecto

Jardinería y Piscinas es una aplicación web desarrollada con **Django** y **Bootstrap**, diseñada para ofrecer un sistema de pedidos online para servicios de jardinería, mantenimiento de piscinas, poda de árboles y corte de césped. La aplicación está optimizada para facilitar la gestión de solicitudes sin necesidad de base de datos, enviando los pedidos directamente a WhatsApp.

## 🚀 Características Implementadas

✅ **Formulario de Pedidos:** Permite a los clientes solicitar servicios y enviar los datos por WhatsApp.
✅ **Boton de Whatsapp Flotante:** Acceso directo a la Atención Personalizada.
✅ **Diseño Responsivo:** Adaptado para dispositivos móviles y escritorio con Bootstrap.
✅ **Galería de Trabajos:** Sección con imágenes de trabajos realizados.
✅ **Testimonios de Clientes:** Muestra reseñas reales de clientes satisfechos.
✅ **Animaciones y Efectos:** Uso de CSS y Bootstrap para mejorar la experiencia visual.
✅ **Sistema de Navegación:** Menú de navegación con anclas para acceso rápido a secciones.
✅ **Estilos Personalizados:** Archivos CSS separados para `style.css`, `home.css` y `galeria.css`.
✅ **Preparado para Despliegue:** Configurado para ser desplegado en plataformas como Heroku, Railway o Render.

## 🛠 Tecnologías Utilizadas

- **Backend:** Django (Python)
- **Frontend:** Django Templates, Bootstrap 5, CSS3
- **Base de Datos:** No requerida (por el momento, el sistema envía los pedidos por WhatsApp)
- **Despliegue:** Soporte para Heroku, Railway, Render

## 📂 Estructura del Proyecto

```
📂 jardineria
├── 📁 jardineria                  # Aplicación principal
│   ├── settings.py
│   ├── views.py            # Lógica de las vistas
│   ├── urls.py             # Rutas de la aplicación
├── 📁 Pedidos
│   ├── 📁 templates
│   │      ├──  📁 Pedidos
│   │           ├── home.html
│   │           ├── galeria.html
│   │           ├── gracias.html
│   │           ├── pedido_form
│   ├── views.py            # Lógica de las vistas
│   ├── urls.py             # Rutas de la aplicación
├── 📁 templates
├── 📁 static
│   ├── 📁 css
│   │   ├── style.css       # Estilos generales
│   │   ├── home.css        # Estilos específicos de la página de inicio
│   │   ├── galeria.css     # Estilos específicos para la galería
├── manage.py               # Archivo de gestión de Django
```

## 🏗 Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/CristianMarcus/jardineria.git
cd jardineria
```

### 2️⃣ Crear un entorno virtual e instalar dependencias

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre tu navegador y accede a `http://127.0.0.1:8000/`

## 🎨 Mejoras Futuras

- Integración con bases de datos para gestionar pedidos.
- Panel de administración para gestionar servicios y clientes.
- Implementación de pasarelas de pago.
- Opciones de personalización para los clientes que compren la aplicación.

## 📞 Contacto

Si tienes dudas o sugerencias, puedes contactarme en [cristianmarcus34@gmail.com](mailto\:cristianmarcus34@gmail.com).

---

✨ *Desarrollado con pasión y dedicación para ofrecer un servicio de calidad.*





