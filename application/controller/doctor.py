from passlib.context import CryptContext
from starlette import status

from application.models.doctor import Doctor
from application.models.schema import doctor as DoctorSchema
from application.models.speciality import Specialization
from application.utils.api_response import CustomException, SuccessResponse

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_doctor(schema: DoctorSchema.DoctorCreate):
    # hash password
    hash_password = Hash.bcrypt(schema.password)
    data = schema.dict()

    # check if doctor with email already exist return 400 bad request
    existing_doctor = Doctor.get_doctor_by_email(data.get('email'))
    if existing_doctor:
        raise CustomException(error="Email already in use")

    # verify doctor domain is exist
    speciality = Specialization.get_speciality_by_title(data.get('speciality'))

    if speciality is None:
        raise CustomException(error="Speciality not supported.")

    data['password'] = hash_password
    doctor = Doctor.create(data)
    return SuccessResponse(data=doctor).setStatusCode(status=status.HTTP_201_CREATED).response()


def delete_doctor(id: int):
    doctor = Doctor.delete(id=id)

    # if doctor with id doesn't exist return 404
    if doctor is None:
        raise CustomException(error=f"Doctor with id {id} not found", status=status.HTTP_404_NOT_FOUND)

    return SuccessResponse(data={}, message=doctor).response()



class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_password, hashed_password):
        return pwd_cxt.verify(hash=hashed_password, secret=plain_password)
