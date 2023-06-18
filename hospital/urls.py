from django.urls import path
from hospital import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
    path('general', views.general, name='general'),
    path('cardiology', views.cardiology, name='cardiology'),
    path('orthopaedics', views.orthopaedics, name='orthopaedics'),
    path('neuro', views.neuro, name='neuro'),
    path('psychiatry', views.psychiatry, name='psychiatry'),
    path('pulmonology', views.pulmonology, name='pulmonology'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]