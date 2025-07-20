from django.contrib import admin
from .models import Doctor, Patient, Room, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'fio', 'available', 'specialty')
    readonly_fields = ('doctor_id',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'fio', 'birth_date', 'patient_age', 'notes', 'prescriptions')
    readonly_fields = ('patient_id',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'available')
    readonly_fields = ('room_id',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'doctor', 'patient', 'room', 'date', 'notes', 'prescriptions', 'cancelled')
    readonly_fields = ('appointment_id',)
