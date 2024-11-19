from django.shortcuts import render, get_object_or_404
from .models import Patient
from .forms import PatientForm

def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients})

def patients_detail(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'patients/patients_detail.html', {'patient': patient})

def patients_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patients_form.html', {'form': form})

def patients_edit(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patients_form.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients})

def patients_detail(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'patients/patients_detail.html', {'patient': patient})

def patients_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patients_form.html', {'form': form})


