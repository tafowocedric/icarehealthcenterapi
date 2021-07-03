from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Table, DATE
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func

from application import Base_Model
from application.database.connection import session_hook
from application.models.schema import appointment as AppointmentSchema

class Appointment(Base_Model):
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctors = relationship('Doctor', backref='appointments')
    patients = relationship('Patient', backref='appointments')
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    date = Column(DateTime, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @staticmethod
    @session_hook
    def get_appointment_by_date(db: Session, date):
        appointment = db.query(Appointment).filter(Appointment.date.cast(DATE)==date).first()
        if appointment is None:
            return None

        return AppointmentSchema._Appointment.from_orm(appointment)

    @staticmethod
    @session_hook
    def get_appointment_by_doctor_id_and_date(db: Session, id, date):
        appointment = db.query(Appointment).filter(Appointment.date.cast(DATE)==date, Appointment.doctor_id==id).first()
        if appointment is None:
            return None

        return AppointmentSchema._Appointment.from_orm(appointment)

    @staticmethod
    @session_hook
    def create(db: Session, data):
        appointment = Appointment(**data)
        db.add(appointment)
        db.flush()

        return AppointmentSchema._Appointment.from_orm(appointment)

    @staticmethod
    @session_hook
    def delete(db:Session, id: int):
        response = db.query(Appointment).filter(Appointment.id==id).delete()
        db.flush()

        # no record found  with id
        if response==0:
            return None

        return "Appointment cancelled successfully"