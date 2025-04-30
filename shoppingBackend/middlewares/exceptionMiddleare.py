from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging

class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logging.error(f"Unhandled error {e}")
            
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"}
            )