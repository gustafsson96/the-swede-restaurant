from django.shortcuts import render
from django.views import generic
from .models import Booking


def home(request):
    return render(request, 'home.html', {})


class ReservationsList(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "reservations.html"
