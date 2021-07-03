from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, root_validator

from application.models.schema.utils import SuccessResponse
from application.utils.api_response import CustomException


class BaseDoctor(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class DoctorCreate(BaseDoctor):
    password: str

    @root_validator(pre=True)
    def check(cls, values):
        errors = []
        for k, v in values.items():
            if v=='string':
                errors.append({k: f'{k.replace("_", " ")} is required'})

        if errors:
            raise CustomException(error=[error for error in errors])

        return values


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
