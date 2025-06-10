# whiteboard_project/urls.py
from django.contrib import admin
from django.urls import path, include
from whiteboard import views as wb_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whiteboard/', include('whiteboard.urls')),
    path('', wb_views.homepage, name='homepage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)