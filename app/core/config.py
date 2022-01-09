import secrets
from typing import Any, Dict, List, Optional, Union
import os
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Fastapi peewee'
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    authjwt_secret_key: str =  secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    CELERY_BROKER_URL = 'amqp://{user}:{password}@{hostname}:{port}/'.format(
        user=os.environ.get('RABBITMQ_DEFAULT_USER', 'guest'),
        password=os.environ.get('RABBITMQ_DEFAULT_PASS', 'guest'),
        port=os.environ.get('RABBITMQ_PORT', '5672'),
        hostname=os.environ.get('RABBITMQ_HOST', 'rabbit')
    )

    class Config:
        case_sensitive = True


settings = Settings()