from fastapi import FastAPI, Request, HTTPException, status, Depends, Security
from fastapi.security.api_key import APIKeyHeader
import time

from api.routes import router as math_router
from services.logger import logger

API_KEY = "secret123"
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI(title="Math Service API")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round((time.time() - start) * 1000, 2)
    logger.info(
        f"{request.method} {request.url.path} [{response.status_code}] took {duration}ms"
    )
    return response


app.include_router(
    math_router,
    dependencies=[Depends(verify_api_key)]
)
