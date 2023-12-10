from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Adminka change texts
admin.site.site_header = "TELEKOM-XIZ.UZ"
admin.site.site_title = "TELEKOM Admin"
admin.site.index_title = "Dashboard!"

# Site urls
urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', include('main_app.urls')),
    path('servislar/', include('service_app.urls')),
    path('yangiliklar/', include('news_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)