from typing import Any

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class SuccessResponse:
    result = {"success": True, "message": "success", "data": Any}

    def __init__(self, data: Any, message: str = None):
        self.data = data
        self.result['data'] = data

        if message is not None:
            self.result["message"] = message
        self.status = status.HTTP_200_OK

    def setMessage(self, message: str):
        self.result['message'] = message
        return self

    def setStatusCode(self, status: int):
        self.status = status
        return self

    def __call__(self):
        return JSONResponse(content=jsonable_encoder(self.result), status_code=self.status)

    def response(self):
        return JSONResponse(content=jsonable_encoder(self.result), status_code=self.status)


# Custom error route response
class CustomException(Exception):
    def __init__(self, error=None, status: int = status.HTTP_400_BAD_REQUEST):
        self.error = error
        self.status = status
