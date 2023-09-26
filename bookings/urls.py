from django.urls import path
from . import views
from bookings.views import get_booking_information, add_reservation, edit_reservation

urlpatterns = [
    path("", views.home, name="home"),
    path("reservations.html", get_booking_information,
         name="reservations"),
    path("add", add_reservation, name="add"),
    path("edit/<item_id>", edit_reservation, name="edit"),
]
