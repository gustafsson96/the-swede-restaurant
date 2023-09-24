from django.shortcuts import render
from django.views import generic
from .models import Booking


def home(request):
    return render(request, 'home.html', {})


def all_reservations(request):
    reservations = Booking.objects.all()
    return render(request, 'reservations.html', 
    {'reservations': reservations})
