from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import connection


class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.CharField(max_length=255)
    birth_date = models.DateField()
    available = models.BooleanField(default=True)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fio} ({self.specialty})'
    

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.CharField(max_length=255)
    birth_date = models.DateField()
    patient_age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    notes = models.TextField(blank=True, null=True)
    prescriptions = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.fio


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.room_id:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT MIN(r1.room_id + 1) 
                    FROM new_app_room r1 
                    LEFT JOIN new_app_room r2 ON r1.room_id + 1 = r2.room_id 
                    WHERE r2.room_id IS NULL
                """)
                row = cursor.fetchone()
                self.room_id = row[0] or 1
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room_name} (ID: {self.room_id})"
    

class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    prescriptions = models.JSONField(default=dict, blank=True)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f'Прием {self.patient} у {self.doctor} в {self.date}'