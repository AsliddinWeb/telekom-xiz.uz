from django.urls import path

from .views import service_home, service_detail

urlpatterns = [
    path('', service_home, name='service_home'),
    path('<slug:slug>/', service_detail, name='service_detail'),
]