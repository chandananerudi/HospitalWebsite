from django.db import models

# Create your models here.

class PatientDetails(models.Model):
    p_first_name = models.CharField(max_length=50, verbose_name="Patient First Name:")
    p_last_name = models.CharField(max_length=50, verbose_name="Patient last Name:")
    p_age = models.IntegerField(verbose_name="Patient Age:")
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('None', 'None'),
    )
    p_gender = models.CharField(max_length=20, choices=GENDER, default='None', verbose_name="Patient Gender:")
    p_phone_number = models.IntegerField(verbose_name="Patient Phone Number:")
    p_email_id = models.EmailField(max_length=100, verbose_name="Patient EmailId:")
    DEPARTMENTS = (
        ('General CheckUp', 'General CheckUp'),
        ('Cardiology', 'Cardiology'),
        ('Pulmonology', 'Pulmonology'),
        ('Psychiatry', 'Psychiatry'),
        ('Neuro Surgery', 'Neuro Surgery'),
        ('Orthopaedics', 'Orthopaedics'),
    )
    p_department = models.CharField(max_length=100, choices=DEPARTMENTS, default='General CheckUp', verbose_name="Health Department")
    p_application_date_time = models.DateTimeField(null=True, verbose_name="Patient Application date and time:")
    p_health_problem = models.TextField(verbose_name="Brief Explanation of health problem:")

    class Meta:
        ordering = ['p_last_name', 'p_first_name']

    def __str__(self):
        return f'{self.p_last_name}, {self.p_first_name}'

class DoctorDetails(models.Model):
    d_first_name = models.CharField(max_length=100, verbose_name="Doctor First Name:")
    d_last_name = models.CharField(max_length=100, verbose_name="Doctor Last Name:")
    d_age = models.IntegerField(verbose_name="Doctor Age:")
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('None', 'None'),
    )
    d_gender = models.CharField(max_length=100, choices=GENDER, default='None', verbose_name="Doctor Gender:")
    d_phone_number = models.IntegerField(verbose_name="Doctor Phone Number:")
    d_email_id = models.EmailField(max_length=100, verbose_name="Doctor EmailId:")
    d_address = models.TextField(verbose_name="Doctor Address")
    DEPARTMENTS = (
        ('General CheckUp', 'General CheckUp'),
        ('Cardiology', 'Cardiology'),
        ('Pulmonology', 'Pulmonology'),
        ('Psychiatry', 'Psychiatry'),
        ('Neuro Surgery', 'Neuro Surgery'),
        ('Orthopaedics', 'Orthopaedics'),
    )
    d_department = models.CharField(max_length=100, choices=DEPARTMENTS, blank=True, default='General CheckUp')

    class Meta:
        ordering = ['d_last_name', 'd_first_name']

    def __str__(self):
        return f'{self.d_last_name}, {self.d_first_name}'

