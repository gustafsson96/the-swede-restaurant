from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reservations.html', views.all_reservations, name="reservations"),
]
