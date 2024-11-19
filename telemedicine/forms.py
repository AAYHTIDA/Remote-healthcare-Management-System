from django import forms
from .models import Telemedicine

class TelemedicineForm(forms.ModelForm):
    class Meta:
        model = Telemedicine
        fields = ['patient', 'consultation_date', 'consultation_time', 'doctor', 'notes']
