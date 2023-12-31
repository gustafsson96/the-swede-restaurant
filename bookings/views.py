from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import ReservationForm


def home(request):
    return render(request, 'home.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def reservation_login(request):
    return render(request, 'make_reservation_login.html', {})


def get_booking_information(request):
    """
    Show booking details specific to logged in user
    """
    information = Booking.objects.filter(user=request.user)
    information_items = {
        'information': information
    }
    return render(request, 'reservations.html', information_items)


def add_reservation(request):
    """
    Create and validate a new reservation
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your reservation has been created!')
            return redirect('reservations')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'add_reservations.html', context)


def edit_reservation(request, item_id):
    """
    Edit an existing reservation
    """
    reservation = get_object_or_404(Booking, id=item_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your reservation was updated successfully!')
            return redirect('reservations')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, item_id):
    """
    Delete an existing reservation
    """
    reservation = get_object_or_404(Booking, id=item_id)
    reservation.delete()
    messages.add_message(request, messages.ERROR,
                         'Your reservation has been cancelled.')
    return redirect('reservations')


def contact(request):
    return render(request, 'contact.html', {})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
