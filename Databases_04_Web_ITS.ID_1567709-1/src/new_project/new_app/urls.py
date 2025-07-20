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
    path('doctor/edit/<uuid:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<uuid:doc_id>/', views.doctor_info, name='doctor_info'),
    path('doctors/export/csv/', views.export_doctors_csv, name='export_doctors_csv'),
    path('doctors/export/json/', views.export_doctors_json, name='export_doctors_json'),
    path('doctors/import/', views.import_doctors, name='import_doctors'),
]
