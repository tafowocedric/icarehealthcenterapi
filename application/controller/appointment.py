from datetime import datetime

from starlette import status

from application.models.appointment import Appointment
from application.models.doctor import Doctor
from application.models.schema import appointment as AppointmentSchema
from application.utils.api_response import CustomException, SuccessResponse


def create_appointment(patient_id: int, schema: AppointmentSchema.AppointmentCreate):
    data = schema.dict()
    data['patient_id'] = patient_id
    appointment_date = data.get("date")

    # check if doctor exist return 400 bad request
    doctor = Doctor.get_doctor_by_id(id=data['doctor_id'])
    if doctor is None:
        raise CustomException(error=f"Doctor with id {data['doctor_id']} doesn't exist")

    # check if appointment date < present date return 400 bad request
    if datetime.timestamp(appointment_date) < datetime.timestamp(datetime.now()):
        raise CustomException(error='Can not book appointment for past date')

    # check if appointment exist for date return 400 bad request
    existing_appointment = Appointment.get_appointment_by_doctor_id_and_date(id=data.get('doctor_id'), date=appointment_date.date())
    if existing_appointment:
        raise CustomException(error="Doctor is already booked for this day")

    appointment = Appointment.create(data)
    return SuccessResponse(data=appointment, message="Appointment successfully Created").setStatusCode(status=status.HTTP_201_CREATED).response()


def delete_appointment(id: int):
    appointment = Appointment.delete(id=id)

    # if appointment with id doesn't exist return 404
    if appointment is None:
        raise CustomException(error=f"Appointment with id {id} not found", status=status.HTTP_404_NOT_FOUND)

    return SuccessResponse(data={}, message=appointment).response()
