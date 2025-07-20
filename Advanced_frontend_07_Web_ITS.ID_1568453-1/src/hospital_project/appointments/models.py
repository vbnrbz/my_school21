import uuid
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.TextField()
    available = models.BooleanField(default=True)
    specialty = models.TextField()

    def __str__(self):
        return self.fio

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.TextField()
    birth_date = models.DateField()
    patient_age = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    prescriptions = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        self.patient_age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.fio

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name

class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    prescriptions = models.JSONField(blank=True, null=True)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment {self.appointment_id}"

class CustomUser(AbstractUser):
    doctor = models.OneToOneField(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')

    def __str__(self):
        return self.username
