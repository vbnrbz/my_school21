from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('doctors/', views.doctors, name='doctors'),
    path('services/', views.services, name='services'),
    path('room/all/', views.room_list, name='room_list'), 
    path('doctor/create/', views.create_doctor, name='create_doctor'),
]
