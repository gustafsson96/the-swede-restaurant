from django.shortcuts import render
from django.views import generic
from .models import Booking


class ReservationList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'reservations.html'
