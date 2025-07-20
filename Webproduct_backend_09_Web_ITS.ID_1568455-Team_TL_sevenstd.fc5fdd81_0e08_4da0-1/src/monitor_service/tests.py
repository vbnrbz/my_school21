import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.models import Patient
from app.routes import get_patients
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_get_patients_function_unit():
    # Создаем MagicMock для результата вызова scalars().all()
    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [Patient(id="1", name="Unit Test Patient")]

    # Создаем объект, который scalars() вернет mock_scalars
    mock_result = MagicMock()
    mock_result.scalars.return_value = mock_scalars

    # Мокаем execute, чтобы он был awaitable и возвращал mock_result
    fake_session = AsyncMock()
    fake_session.execute.return_value = mock_result  # здесь НЕ корутина, а просто MagicMock

    # Патчим async_session на возвращение fake_session
    with patch("app.routes.async_session", return_value=fake_session):
        patients = await get_patients(fake_session)
        assert len(patients) == 1
        assert patients[0].name == "Unit Test Patient"

def test_get_patients_endpoint():
    response = client.get("/patients")
    assert response.status_code in (200, 404)
