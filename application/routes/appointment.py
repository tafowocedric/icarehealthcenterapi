from fastapi import APIRouter

from application.controller import appointment as AppointmentController
from application.models.schema import appointment as AppointmentSchema
from application.models.schema.utils import SuccessResponse

router = APIRouter(prefix='/appointments', tags=['appointments'])


@router.post("/create/{patient_id}", response_model=AppointmentSchema.Appointment)
def create_appointment(patient_id: int, schema: AppointmentSchema.AppointmentCreate):
    return AppointmentController.create_appointment(patient_id, schema=schema)


@router.get("/delete/{id}", response_model=SuccessResponse)
def delete_appointment(id: int):
    return AppointmentController.delete_appointment(id=id)
