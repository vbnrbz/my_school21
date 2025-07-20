# appointments/tests/test_models.py

import datetime
import pytest
from appointments.models import Patient, Doctor


@pytest.mark.django_db
def test_patient_age_is_calculated_correctly():
    birth_date = datetime.date(1990, 6, 16)
    patient = Patient.objects.create(fio="Иван Иванов", birth_date=birth_date)
    today = datetime.date.today()

    expected_age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

    assert patient.patient_age == expected_age, \
        f"Expected age {expected_age}, got {patient.patient_age}"


@pytest.mark.django_db
def test_doctor_creation_and_str():
    doctor = Doctor.objects.create(
        fio="Доктор Хаус", specialty="Диагностика", available=True
    )
    assert str(doctor) == "Доктор Хаус"
    assert doctor.specialty == "Диагностика"
    assert doctor.available is True
