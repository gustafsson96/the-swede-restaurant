from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking
from .forms import ReservationForm


def home(request):
    return render(request, 'home.html', {})


def get_booking_information(request):
    information = Booking.objects.all()
    information_items = {
        'information': information
    }
    return render(request, 'reservations.html', information_items)


def add_reservation(request):
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'add_reservations.html', context)
