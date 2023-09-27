from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reservations.html", views.get_booking_information,
         name="reservations"),
    path("add", views.add_reservation, name="add"),
    path("edit/<item_id>", views.edit_reservation, name="edit"),
    path("delete/<item_id>", views.delete_reservation, name="delete"),
    path("menu", views.menu, name="menu"),
    path("contact", views.contact, name="contact"),
    path("reservation_login", views.reservation_login, name="reservation_login"),
]
