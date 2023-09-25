from .models import Booking
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'number_of_guests', 'message']