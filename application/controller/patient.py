from starlette import status

from application.models.patient import Patient
from application.models.schema import patient as PatientSchema
from application.utils.api_response import CustomException, SuccessResponse
from application.utils.bcrypt import Hash


def create_patient(schema: PatientSchema.PatientCreate):
    # hash password
    hash_password = Hash.bcrypt(schema.password)
    data = schema.dict()

    # check if patient with phone number already exist return 400 bad request
    existing_patient = Patient.get_patient_by_phone(data.get('phone'))
    if existing_patient:
        raise CustomException(error="Phone number already in use")

    data['password'] = hash_password
    patient = Patient.create(data)
    return SuccessResponse(data=patient).setStatusCode(status=status.HTTP_201_CREATED).response()


def delete_patient(id: int):
    patient = Patient.delete(id=id)

    # if patient with id doesn't exist return 404
    if patient is None:
        raise CustomException(error=f"Patient with id {id} not found", status=status.HTTP_404_NOT_FOUND)

    return SuccessResponse(data={}, message=patient).response()
