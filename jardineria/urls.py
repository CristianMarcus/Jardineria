from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Asegúrate de incluir las URLs de tu app 'core'
]

# Solo en desarrollo, sirve archivos de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
