import pytest
import datetime
from rest_framework.test import APIClient
from appointments.models import Doctor, Patient, Room, Appointment
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_create_appointment_api():
    client = APIClient()

    doctor = Doctor.objects.create(
        fio="Доктор Кто",
        specialty="Кардиология",
        available=True
    )
    patient = Patient.objects.create(
        fio="Пётр Петров",
        birth_date=datetime.date(1990, 1, 1)
    )
    room = Room.objects.create(room_name="Кабинет 101")

    # Используем timezone-aware datetime
    appointment_time = timezone.now() + datetime.timedelta(days=2)
    appointment_time = appointment_time.replace(
        hour=10, minute=0, second=0, microsecond=0
    )

    data = {
        "doctor": str(doctor.doctor_id),
        "patient": str(patient.patient_id),
        "room": room.room_id,
        "date": appointment_time.isoformat()
    }

    response = client.post("/api/appointments/create", data, format="json")

    assert response.status_code == 201, f"Unexpected response: {response.content}"

    created_appointment = Appointment.objects.first()
    assert created_appointment is not None
    assert created_appointment.doctor == doctor
    assert created_appointment.patient == patient
    assert created_appointment.room == room
    assert created_appointment.date == appointment_time


@pytest.mark.django_db
def test_register_patient_without_birth_date():
    client = APIClient()
    data = {
        "username": "test_user",
        "password": "testpass123",
        "fio": "Алексей Смирнов"
        # birth_date отсутствует
    }

    response = client.post("/api/register/patient", data, format="json")

    # Проверка ошибки валидации
    assert response.status_code == 400

    from django.contrib.auth import get_user_model
    User = get_user_model()

    # Проверка, что пользователь не создан
    assert User.objects.filter(username="test_user").count() == 0
    assert Patient.objects.filter(fio="Алексей Смирнов").count() == 0
