from datetime import datetime
from dateutil import parser

from starlette import status

from application.models.appointment import Appointment
from application.models.schema import appointment as AppointmentSchema
from application.utils.api_response import CustomException, SuccessResponse



def create_appointment(patient_id: int, schema: AppointmentSchema.AppointmentCreate):
    data = schema.dict()
    data['patient_id'] = patient_id
    appointment_date = data.get("date")

    # check if appointment date < present date return 400 bad request
    if datetime.timestamp(appointment_date) < datetime.timestamp(datetime.now()):
        raise CustomException(error='Can not book appointment for past date')

    # check if appointment exist for date return 400 bad request
    existing_appointment = Appointment.get_appointment_by_doctor_id_and_date(id=data.get('doctor_id'), date=appointment_date.date())
    if existing_appointment:
        raise CustomException(error="Doctor is already booked for this day")

    appointment = Appointment.create(data)
    return SuccessResponse(data=appointment).response()


def delete_appointment(id: int):
    appointment = Appointment.delete(id=id)

    # if appointment with id doesn't exist return 404
    if appointment is None:
        raise CustomException(error=f"Appointment with id {id} not found", status=status.HTTP_404_NOT_FOUND)

    return SuccessResponse(data={}, message=appointment).response()


