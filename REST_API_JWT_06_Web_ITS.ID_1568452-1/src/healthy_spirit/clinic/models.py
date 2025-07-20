import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    fio = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    fio = models.CharField(max_length=255)
    birth_date = models.DateField()
    patient_age = models.IntegerField(editable=False)
    notes = models.TextField(blank=True)
    prescriptions = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        self.patient_age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        super().save(*args, **kwargs)

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    prescriptions = models.JSONField(default=list)
    cancelled = models.BooleanField(default=False)