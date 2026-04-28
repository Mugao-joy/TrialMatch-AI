from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    diagnosis = Column(String)
    age = Column(String)
    gender = Column(String)
    location = Column(String)

    trials = relationship("Trial", back_populates="patient")


class Trial(Base):
    __tablename__ = "trials"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    trial_title = Column(String)
    nct_id = Column(String)
    match_score = Column(Integer)
    reason = Column(String)

    patient = relationship("Patient", back_populates="trials")