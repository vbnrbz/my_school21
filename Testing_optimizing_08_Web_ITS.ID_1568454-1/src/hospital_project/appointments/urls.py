from django.urls import path
from .views import (
    RoomCreateAPIView,
    RoomListAPIView,
    RoomRetrieveUpdateDestroyAPIView,
    DoctorRetrieveUpdateAPIView,
    DoctorAppointmentsAPIView,
    PatientRetrieveUpdateAPIView,
    PatientAddPrescriptionsAPIView,
    AppointmentCreateAPIView,
    CancelAppointmentAPIView,
    DoctorRegisterAPIView,
    PatientRegisterAPIView,
    PatientUUIDLookupAPIView,
    DoctorUUIDLookupAPIView,
    DoctorListAPIView,
    PatientListAPIView,
)


urlpatterns = [
    # Эндпойнты для кабинетов (Room)
    path('api/room/create', RoomCreateAPIView.as_view(), name='room-create'),
    path('api/room', RoomListAPIView.as_view(), name='room-list'),
    path('api/room/<int:room_id>', RoomRetrieveUpdateDestroyAPIView.as_view(),
         name='room-detail'),

    # Эндпойнты для докторов
    path('api/doctors/<uuid:doctor_id>', DoctorRetrieveUpdateAPIView.as_view(),
         name='doctor-detail'),
    path('api/doctors/<uuid:doctor_id>/appointments',
         DoctorAppointmentsAPIView.as_view(),
         name='doctor-appointments'),
    path('api/doctors/all', DoctorListAPIView.as_view(),
         name='doctor-list'),  # Новый эндпойнт

    # Эндпойнты для пациентов
    path('api/patients/<uuid:patient_id>',
         PatientRetrieveUpdateAPIView.as_view(),
         name='patient-detail'),
    path('api/patients/<uuid:patient_id>/prescriptions',
         PatientAddPrescriptionsAPIView.as_view(),
         name='patient-add-prescriptions'),
    path('api/patients/all', PatientListAPIView.as_view(),
         name='patient-list'),  # Новый эндпойнт

    # Эндпойнты для встреч (Appointment)
    path('api/appointments/create',
         AppointmentCreateAPIView.as_view(), name='appointment-create'),
    path('api/appointments/cancel',
         CancelAppointmentAPIView.as_view(), name='appointment-cancel'),

    # Эндпойнты для регистрации
    path('api/register/doctor',
         DoctorRegisterAPIView.as_view(), name='doctor-register'),
    path('api/register/patient',
         PatientRegisterAPIView.as_view(), name='patient-register'),

    # Новые эндпойнты для поиска UUID по параметрам
    path('api/patients/lookup',
         PatientUUIDLookupAPIView.as_view(), name='patient-lookup'),
    path('api/doctors/lookup',
         DoctorUUIDLookupAPIView.as_view(), name='doctor-lookup'),
]
