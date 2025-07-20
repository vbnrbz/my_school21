import uuid
import datetime
from django.db import models

class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.TextField(verbose_name="ФИО врача")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    specialty = models.TextField(verbose_name="Специальность")

    def __str__(self):
        return self.fio

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.TextField(verbose_name="ФИО пациента")
    birth_date = models.DateField(verbose_name="Дата рождения")
    patient_age = models.IntegerField(verbose_name="Возраст", blank=True, null=True)
    notes = models.TextField(verbose_name="Примечания", blank=True, null=True)
    prescriptions = models.JSONField(verbose_name="Рецепты", blank=True, null=True)

    def __str__(self):
        return self.fio

    def save(self, *args, **kwargs):
        if self.birth_date:
            today = datetime.date.today()
            self.patient_age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        super().save(*args, **kwargs)

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, verbose_name="Номер кабинета")
    room_name = models.TextField(verbose_name="Название кабинета")
    available = models.BooleanField(default=True, verbose_name="Доступен")

    def __str__(self):
        return self.room_name

class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, db_column='room_number', verbose_name="Кабинет")
    date = models.DateTimeField(verbose_name="Дата и время")
    notes = models.TextField(verbose_name="Примечания")
    prescriptions = models.JSONField(
        verbose_name="Рецепты",
        help_text='Пример: {"drug1": "paracetamol", "drug2": "validol"}'
    )
    cancelled = models.BooleanField(default=False, verbose_name="Отменено")

    def __str__(self):
        return f"Запись {self.appointment_id}"
