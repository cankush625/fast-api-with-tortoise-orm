from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.core.urls import api_router
from server.config.settings import settings


def create_app() -> FastAPI:
    current_app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        current_app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    current_app.include_router(api_router, prefix=settings.API_V1_STR)
    return current_app


app = create_app()
