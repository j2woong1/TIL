from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
    ))
    class Meta:
        model = Reservation
        fields = '__all__'