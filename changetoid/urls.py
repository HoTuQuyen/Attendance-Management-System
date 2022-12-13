from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from changetoid import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workapp.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
