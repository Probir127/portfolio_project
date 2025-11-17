from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')), 
]

# Essential for serving static and media files during development
if settings.DEBUG:
    # Serve media files (project images)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files (profile pic, css)
    # Note: STATIC_ROOT is primarily for production, but using STATIC_URL helps in dev
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)