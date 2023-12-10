from django.urls import path

from .views import news_detail

urlpatterns = [
    path('<slug:slug>/', news_detail, name='news_detail'),
]