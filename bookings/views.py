from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import ReservationForm


def home(request):
    return render(request, 'home.html', {})


def menu(request):
    return render(request, 'menu.html', {})


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


def edit_reservation(request, item_id):
    reservation = get_object_or_404(Booking, id=item_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('reservations')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, item_id):
    reservation = get_object_or_404(Booking, id=item_id)
    reservation.delete()
    return redirect('reservations')


def contact(request):
    return render(request, 'contact.html', {})