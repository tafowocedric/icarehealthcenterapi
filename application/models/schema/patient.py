from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from application.models.schema.utils import SuccessResponse


class BasePatient(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str]
    phone: str


class PatientCreate(BasePatient):
    password: str


class _Patient(BasePatient):
    id: Optional[int]
    full_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Patient(SuccessResponse):
    data: Optional[_Patient]


class PatientList(SuccessResponse):
    data: Optional[List[_Patient]]
