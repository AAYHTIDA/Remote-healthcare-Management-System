from django.shortcuts import render, redirect
from .models import Telemedicine
from .forms import TelemedicineForm

def telemedicine_list(request):
    telemedicine_records = Telemedicine.objects.all()
    return render(request, 'telemedicine/telemedicine_list.html', {'telemedicine_records': telemedicine_records})

def telemedicine_detail(request, id):
    record = Telemedicine.objects.get(id=id)
    return render(request, 'telemedicine/telemedicine_detail.html', {'record': record})

def telemedicine_create(request):
    if request.method == 'POST':
        form = TelemedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('telemedicine_list')
    else:
        form = TelemedicineForm()
    return render(request, 'telemedicine/telemedicine_form.html', {'form': form})

def telemedicine_edit(request, id):
    record = Telemedicine.objects.get(id=id)
    if request.method == 'POST':
        form = TelemedicineForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('telemedicine_list')
    else:
        form = TelemedicineForm(instance=record)
    return render(request, 'telemedicine/telemedicine_form.html', {'form': form})

