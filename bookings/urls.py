from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reservations.html", views.get_booking_information,
         name="reservations"),
]
