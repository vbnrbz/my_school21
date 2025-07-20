from django.urls import path
from .views import doctors_list, create_doctor_profile, create_patient_profile
from .views import account_view, private_account_view

urlpatterns = [
    path('doctors/', doctors_list, name='doctors_list'),
    path('doctor/create/', create_doctor_profile, name='create_doctor_profile'),
    path('patient/create/', create_patient_profile, name='create_patient_profile'),
    path('account/', account_view, name='account'),
    path('account/private/', private_account_view, name='account_private'),
]