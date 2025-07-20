import logging
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session
from app.models import Patient, PatientMetric

logger = logging.getLogger(__name__)

class DataService:
    @staticmethod
    async def save_patient_data(data: dict):
        async with async_session() as session:
            result = await session.execute(select(Patient).where(Patient.id == data["uuid"]))
            patient = await result.scalar_one_or_none()

            if not patient:
                patient = Patient(id=data["uuid"], name=data["name"])
                session.add(patient)
                logger.info(f"Created new patient with id={patient.id}")

            timestamp = data.get("timestamp")
            if isinstance(timestamp, str):
                try:
                    timestamp = datetime.fromisoformat(timestamp)
                except ValueError as e:
                    logger.error(f"Invalid timestamp format: {timestamp}, error: {e}")
                    timestamp = datetime.utcnow()

            metric = PatientMetric(
                patient_id=patient.id,
                timestamp=timestamp,
                pulse=data.get("pulse"),
                resp_rate=data.get("resp_rate"),
                bp=data.get("bp"),
                spo2=data.get("spo2"),
                temperature=data.get("temperature"),
            )
            session.add(metric)
            await session.commit()
            logger.info(f"Saved metric for patient {patient.id}")
