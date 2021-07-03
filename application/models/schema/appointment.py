from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from application.models.schema.utils import SuccessResponse


class BaseAppointment(BaseModel):
    doctor_id: Optional[int]
    date: datetime


class AppointmentCreate(BaseAppointment):
    description: str


class _Appointment(BaseAppointment):
    id: Optional[int]
    patient_id: Optional[int]
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Appointment(SuccessResponse):
    data: Optional[_Appointment]


class AppointmentList(SuccessResponse):
    data: Optional[List[_Appointment]]
