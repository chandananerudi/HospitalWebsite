from django.contrib import admin
from .models import PatientDetails, DoctorDetails
# Register your models here.

admin.site.register(PatientDetails)
admin.site.register(DoctorDetails)
