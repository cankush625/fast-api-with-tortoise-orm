import secrets
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, HttpUrl, PostgresDsn, EmailStr

load_dotenv()  # take environment variables from .env.


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # Database
    DATABASE_DRIVER = "postgresql+psycopg2"
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_NAME: str
    DATABASE_PORT: int
    DATABASE_URI: Optional[PostgresDsn] = None

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
