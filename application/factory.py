import json

from fastapi import FastAPI, Request, status
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .config import settings

# accept all origins
origins = ["*"]


def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)

    # middlewares
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

    # routes
    # @app.get("/")
    # def read_root():
    #     return {"Hello": "World"}

    # override validation error
    @app.exception_handler(RequestValidationError)
    async def http_exception_handler(request, error):
        errors = []
        for err in json.loads(error.json()):
            errors.append({err['loc'][0]: err['msg']})

        return JSONResponse(content={'success': False, "data": {"error": errors}}, status_code=status.HTTP_400_BAD_REQUEST)

    from .api_response import CustomException
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(status_code=exc.status, content={'success': False, 'error': {"data": exc.error}})

    return app