from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func

from application import Base_Model
from application.database.connection import session_hook
from application.models.schema import patient as PatientSchema


class Patient(Base_Model):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100), unique=True)
    password = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    @session_hook
    def get_patient_by_phone(db: Session, phone):
        patient = db.query(Patient).filter(Patient.phone==phone).first()
        if patient is None:
            return None

        return PatientSchema._Patient.from_orm(patient)

    @staticmethod
    @session_hook
    def create(db: Session, data):
        patient = Patient(**data)
        db.add(patient)
        db.flush()

        return PatientSchema._Patient.from_orm(patient)

    @staticmethod
    @session_hook
    def delete(db: Session, id: int):
        response = db.query(Patient).filter(Patient.id==id).delete()
        db.flush()

        # no record found  with id
        if response==0:
            return None

        return "Account deleted successfully"
