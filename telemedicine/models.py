
from django.db import models
from patients.models import Patient
from staff.models import Staff

class Telemedicine(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    consultation_date = models.DateField()
    consultation_time = models.TimeField()
    doctor = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Telemedicine consultation with {self.patient} on {self.consultation_date}"


