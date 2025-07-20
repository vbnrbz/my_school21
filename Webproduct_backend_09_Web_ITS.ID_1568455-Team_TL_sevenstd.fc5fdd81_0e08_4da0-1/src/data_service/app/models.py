from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import uuid
from datetime import datetime

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)

    metrics = relationship("PatientMetric", back_populates="patient")

class PatientMetric(Base):
    __tablename__ = 'patient_metrics'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey("patients.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    pulse = Column(Integer)
    resp_rate = Column(Integer)
    bp = Column(String)  # e.g. "120/80"
    spo2 = Column(Float)
    temperature = Column(Float)

    patient = relationship("Patient", back_populates="metrics")
