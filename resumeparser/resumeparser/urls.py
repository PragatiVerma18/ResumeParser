from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path, include
from django.conf.urls.static import static
import start

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('start.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
