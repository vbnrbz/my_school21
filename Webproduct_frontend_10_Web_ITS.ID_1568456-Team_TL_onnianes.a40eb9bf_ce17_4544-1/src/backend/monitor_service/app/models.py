import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = sa.Column(sa.String, primary_key=True, index=True)
    name = sa.Column(sa.String, nullable=False)

    metrics = relationship("PatientMetric", back_populates="patient")


class PatientMetric(Base):
    __tablename__ = "patient_metrics"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    patient_id = sa.Column(sa.String, sa.ForeignKey("patients.id"), nullable=False)
    timestamp = sa.Column(sa.DateTime, nullable=False)
    pulse = sa.Column(sa.Integer)
    resp_rate = sa.Column(sa.Integer)
    bp = sa.Column(sa.String)
    spo2 = sa.Column(sa.Float)
    temperature = sa.Column(sa.Float)

    patient = relationship("Patient", back_populates="metrics")
