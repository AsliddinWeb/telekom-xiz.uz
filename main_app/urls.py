from django.urls import path

from .views import home_page, contact_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contact/', contact_page, name='contact_page'),
]