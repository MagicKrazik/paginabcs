from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('audiencias/', views.audiencias, name='audiencias'),
    path('cartografia/', views.cartografia_view, name='cartografia'),
]