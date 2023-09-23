from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reservations.html', views.reservations, name="reservations"),
]
