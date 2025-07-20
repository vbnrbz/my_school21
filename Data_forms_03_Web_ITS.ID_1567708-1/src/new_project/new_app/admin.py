from django.contrib import admin
from .models import Doctor, Patient, Room, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'fio', 'birth_date', 'available', 'specialty')
    search_fields = ('fio', 'specialty')
    list_filter = ('available', 'specialty')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'fio', 'birth_date', 'patient_age')
    search_fields = ('fio',)
    list_filter = ('birth_date',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'available')
    list_editable = ('room_name', 'available')
    ordering = ('room_id',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'doctor', 'patient', 'room', 'date', 'cancelled')
    search_fields = ('doctor__fio', 'patient__fio')
    list_filter = ('date', 'cancelled', 'doctor', 'room')
    date_hierarchy = 'date'