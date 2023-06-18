from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PatientDetails
# Create your views here.

def index(request):
    return render(request, 'index.html')

def appointment(request):
    if request.method == "POST":
        p_first_name = request.POST['fname']
        p_last_name = request.POST['lname']
        p_age = request.POST['age']
        p_gender = request.POST['gender']
        p_phone_number = request.POST['phone']
        p_email_id = request.POST['email']
        p_department = request.POST['department']
        # p_application_date_time = request.POST['datetime']
        p_health_problem = request.POST['textarea']

        print(p_first_name, p_last_name)

        new_patient = PatientDetails(p_first_name=p_first_name, p_last_name=p_last_name, p_age=p_age, p_gender=p_gender,
                                     p_phone_number=p_phone_number, p_email_id=p_email_id, p_department=p_department,
                                     p_health_problem=p_health_problem)
        new_patient.save()
    return render(request, 'appointment.html')

def general(request):
    return render(request, 'General_CheckUp.html')

def cardiology(request):
    return render(request, 'cardiology.html')

def orthopaedics(request):
    return render(request, 'orthopaedics.html')

def neuro(request):
    return render(request, 'neuro.html')

def psychiatry(request):
    return render(request, 'psychiatry.html')

def pulmonology(request):
    return render(request, 'pulmonology.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
