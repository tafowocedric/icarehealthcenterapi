from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from application.models.schema import doctor as DoctorSchema
from application.controller import doctor as DoctorController
from application.models.schema.utils import SuccessResponse

router = APIRouter(prefix='/doctors', tags=['doctors'])

@router.post("/create", response_model=DoctorSchema.Doctor)
def create_doctor(schema: DoctorSchema.DoctorCreate):
    return DoctorController.create_doctor(schema=schema)


@router.get("/delete/{id}", response_model=SuccessResponse)
def delete_doctor(id: int):
    return DoctorController.delete_doctor(id=id)
