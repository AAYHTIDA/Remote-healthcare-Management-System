
from django.shortcuts import redirect, render, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm



def appointments_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})

def appointments_detail(request, id):
    appointment = Appointment.objects.get(id=id)
    return render(request, 'appointments/appointments_detail.html', {'appointment': appointment})

def appointments_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointments_form.html', {'form': form})

def appointments_edit(request, id):
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointments_form.html', {'form': form})

