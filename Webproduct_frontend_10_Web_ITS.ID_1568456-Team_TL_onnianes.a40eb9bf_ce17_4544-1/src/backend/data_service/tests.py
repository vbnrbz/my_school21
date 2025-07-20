import pytest
from unittest.mock import AsyncMock, patch
from app.data import DataService
from fastapi.testclient import TestClient
from app.main import app

@pytest.mark.asyncio
async def test_save_patient_data_creates_metric():
    fake_session = AsyncMock()
    fake_session.execute.return_value.scalar_one_or_none.return_value = None
    fake_session.add = AsyncMock()
    fake_session.commit = AsyncMock()

    class AsyncSessionContextManager:
        async def __aenter__(self):
            return fake_session
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    with patch("app.data.async_session", return_value=AsyncSessionContextManager()):
        data = {
            "uuid": "123",
            "name": "Test Patient",
            "timestamp": "2023-01-01T10:00:00",
            "pulse": 70,
            "resp_rate": 16,
            "bp": "120/80",
            "spo2": 98.5,
            "temperature": 36.6,
        }
        await DataService.save_patient_data(data)
        assert fake_session.add.called
        assert fake_session.commit.called

def test_root_endpoint():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}
