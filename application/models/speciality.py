from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func

from application import Base_Model
from application.database.connection import session_hook


class Specialization(Base_Model):
    __tablename__ = 'specialization'

    title = Column(String(100), primary_key=True, unique=True)
    doctors = relationship('Doctor', backref=backref("specialization"), cascade='all, delete')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @staticmethod
    @session_hook
    def get_speciality_by_title(db: Session, title: int):
        speciality = db.query(Specialization).filter(Specialization.title==title).first()
        return speciality

    @staticmethod
    @session_hook
    def get_specialities(db: Session):
        specialities = db.query(Specialization).all()
        return specialities
