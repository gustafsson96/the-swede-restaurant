from .models import Booking
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'number_of_guests', 'message']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            )}
        labels = {
            'name': ('Name '),
            'date': ('Date '),
            'time': ('Time '),
            'number_of_guests': ('Number of Guests '),
            'message': ('Special Requests or Allergy Information? Add here!'),
        }


form = ReservationForm()
