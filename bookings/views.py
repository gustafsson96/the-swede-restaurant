from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('reservations')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'add_reservations.html', context)
