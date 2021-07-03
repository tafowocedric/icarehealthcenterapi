from starlette import status

from application.models.doctor import Doctor
from application.models.schema import doctor as DoctorSchema
from application.utils.api_response import CustomException, SuccessResponse
from application.utils.bcrypt import Hash


def create_doctor(schema: DoctorSchema.DoctorCreate):
    # hash password
    hash_password = Hash.bcrypt(schema.password)
    data = schema.dict()

    # check if doctor with email already exist return 400 bad request
    existing_doctor = Doctor.get_doctor_by_email(data.get('email'))
    if existing_doctor:
        raise CustomException(error="Email already in use")

    data['password'] = hash_password
    doctor = Doctor.create(data)
    return SuccessResponse(data=doctor).setStatusCode(status=status.HTTP_201_CREATED).response()


def delete_doctor(id: int):
    doctor = Doctor.delete(id=id)

    # if doctor with id doesn't exist return 404
    if doctor is None:
        raise CustomException(error=f"Doctor with id {id} not found", status=status.HTTP_404_NOT_FOUND)

    return SuccessResponse(data={}, message=doctor).response()
