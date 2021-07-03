from datetime import datetime
from typing import Optional, Any, List
from pydantic import BaseModel, validator

from application.models.schema.utils import SuccessResponse


class BaseDoctor(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    speciality: Optional[Any]

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