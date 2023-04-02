import os
import environs
import secrets
from typing import Optional

from pydantic import BaseSettings, HttpUrl, EmailStr

ROOT_DIR = environs.Path(__file__).parent.parent  # (config/base.py - 2 = server/)

ENV = environs.Env()
# Make a path to .env file in root directory
ENV_PATH = str(ROOT_DIR._make_child([".env"]))
# If .env file present then only load env it
if os.path.exists(ENV_PATH):
    ENV.read_env(ENV_PATH)

DATABASE_HOST: str = ENV("DATABASE_HOST")
DATABASE_USER: str = ENV("DATABASE_USER")
DATABASE_PASS: str = ENV("DATABASE_PASS")
DATABASE_NAME: str = ENV("DATABASE_NAME")
DATABASE_PORT: str = ENV("DATABASE_PORT")

# Tortoise config is written outside Settings class because
# when performing aerich init for database migrations, it cannot
# access Tortoise config from settings class, but it requires to have
# it defined at global level in file
TORTOISE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.psycopg",
            "credentials": {
                "host": DATABASE_HOST,
                "port": DATABASE_PORT,
                "user": DATABASE_USER,
                "password": DATABASE_PASS,
                "database": DATABASE_NAME,
            },
        },
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "server.core.auth.models"],
            "default_connection": "default",
        }
    },
    "routers": [],
    "use_tz": True,
    "timezone": "UTC",
}


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # TORTOISE config should be used through settings
    TORTOISE_CONFIG = TORTOISE_CONFIG

    # Celery
    @staticmethod
    def route_task(name, args, kwargs, options, task=None, **kw):
        if ":" in name:
            queue, _ = name.split(":")
            return {"queue": queue}
        return {"queue": "celery"}

    # Celery
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERYD_SOFT_TIME_LIMIT = 30 * 60
    CELERYD_TIME_LIMIT = 31 * 60

    PROJECT_NAME: str = "Base FastAPI"
    SENTRY_DSN: Optional[HttpUrl] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/server/core/templates/html/email"
    EMAILS_ENABLED: bool = False

    # Email
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # Timezone
    TIME_ZONE = "UTC"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
