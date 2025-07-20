from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime
import logging

from app.database import async_session
from app.models import Patient, PatientMetric
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter()

class PatientOut(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

class PatientMetricOut(BaseModel):
    timestamp: datetime
    pulse: int | None
    resp_rate: int | None
    bp: str | None
    spo2: float | None
    temperature: float | None

    class Config:
        orm_mode = True

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.get("/patients", response_model=List[PatientOut])
async def get_patients(session: AsyncSession = Depends(get_session)):
    logger.info("Fetching list of patients")
    result = await session.execute(select(Patient))
    patients = result.scalars().all()
    logger.info(f"Returned {len(patients)} patients")
    return patients

@router.get("/patient/{patient_id}/metrics", response_model=List[PatientMetricOut])
async def get_patient_metrics(patient_id: str, session: AsyncSession = Depends(get_session)):
    logger.info(f"Fetching metrics for patient_id={patient_id}")
    result = await session.execute(
        select(PatientMetric).where(PatientMetric.patient_id == patient_id).order_by(PatientMetric.timestamp)
    )
    metrics = result.scalars().all()
    if not metrics:
        logger.warning(f"No metrics found for patient_id={patient_id}")
        raise HTTPException(status_code=404, detail="Metrics not found")
    logger.info(f"Returned {len(metrics)} metrics for patient_id={patient_id}")
    return metrics