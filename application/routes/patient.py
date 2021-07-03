from fastapi import APIRouter

from application.controller import patient as PatientController
from application.models.schema import patient as PatientSchema
from application.models.schema.utils import SuccessResponse

router = APIRouter(prefix='/patients', tags=['patients'])


@router.post("/create", response_model=PatientSchema.Patient)
def create_patient(schema: PatientSchema.PatientCreate):
    return PatientController.create_patient(schema=schema)


@router.get("/delete/{id}", response_model=SuccessResponse)
def delete_patient(id: int):
    return PatientController.delete_patient(id=id)
