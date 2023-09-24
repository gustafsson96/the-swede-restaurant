from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.ReservationsList.as_view(), name="reservations_list"),
]
