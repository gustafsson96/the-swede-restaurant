from django.shortcuts import render
from django.views import generic
from .models import Booking


def home(request):
    return render(request, 'home.html', {})
