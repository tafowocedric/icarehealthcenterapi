from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from application.models.schema.utils import SuccessResponse


class BaseDoctor(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class DoctorCreate(BaseDoctor):
    password: str


class _Doctor(BaseDoctor):
    id: Optional[int]
    full_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Doctor(SuccessResponse):
    data: Optional[_Doctor]


class DoctorList(SuccessResponse):
    data: Optional[List[_Doctor]]
