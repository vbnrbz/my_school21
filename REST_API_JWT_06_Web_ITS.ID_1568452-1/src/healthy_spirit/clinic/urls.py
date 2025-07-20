from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'api/rooms', RoomViewSet, basename='room')
router.register(r'api/doctors', DoctorViewSet, basename='doctor')
router.register(r'api/patients', PatientViewSet, basename='patient')
router.register(r'api/appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/doctor/', DoctorRegisterView.as_view()),
    path('api/register/patient/', PatientRegisterView.as_view()),
    path('api/doctors/lookup/', DoctorLookupView.as_view()),
    path('api/patients/lookup/', PatientLookupView.as_view()),
    path('api/appointments/create/', AppointmentCreateView.as_view()),
    path('api/appointments/<uuid:appointment_id>/cancel/', AppointmentCancelView.as_view()),
]