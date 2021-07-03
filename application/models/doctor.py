from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func

from application import Base_Model
from application.database.connection import session_hook
from application.models.schema import doctor as DoctorSchema


class Doctor(Base_Model):
    __tablename__ = 'doctor'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(100), unique=True)
    password = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    @session_hook
    def get_doctor_by_email(db: Session, email):
        doctor = db.query(Doctor).filter(Doctor.email==email).first()
        if doctor is None:
            return None

        return DoctorSchema._Doctor.from_orm(doctor)

    @staticmethod
    @session_hook
    def get_doctor_by_phone(db: Session, phone):
        doctor = db.query(Doctor).filter(Doctor.phone==phone).first()
        if doctor is None:
            return None

        return DoctorSchema._Doctor.from_orm(doctor)


    @staticmethod
    @session_hook
    def create(db: Session, data):
        doctor = Doctor(**data)
        db.add(doctor)
        db.flush()

        return DoctorSchema._Doctor.from_orm(doctor)

    @staticmethod
    @session_hook
    def delete(db: Session, id: int):
        response = db.query(Doctor).filter(Doctor.id==id).delete()
        db.flush()

        # no record found  with id
        if response==0:
            return None

        return "Account deleted successfully"
