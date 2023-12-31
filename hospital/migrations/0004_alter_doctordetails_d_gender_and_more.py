# Generated by Django 4.2 on 2023-04-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_doctordetails_d_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='d_gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('None', 'None')], default='None', max_length=100, verbose_name='Doctor Gender:'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='p_department',
            field=models.CharField(choices=[('General CheckUp', 'General CheckUp'), ('Cardiology', 'Cardiology'), ('Pulmonology', 'Pulmonology'), ('Psychiatry', 'Psychiatry'), ('Neuro Surgery', 'Neuro Surgery'), ('Orthopaedics', 'Orthopaedics')], default='General CheckUp', max_length=100, verbose_name='Patient Health Department'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='p_gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('None', 'None')], default='None', max_length=20, verbose_name='Patient Gender:'),
        ),
    ]
