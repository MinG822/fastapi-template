from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from application.validators import exception

def exception_handler(app:FastAPI):
    @app.exception_handler(exception.BadRequestException)
    async def handle_bad_request(request: Request, exc: exception.BadRequestException):
        return JSONResponse(
            status_code=400,
            content={
                "error_msg":"Bad Request"
            }
        )

    return app