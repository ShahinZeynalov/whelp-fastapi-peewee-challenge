from app.user.crud import (
    get_user_by_email
)
from typing import Optional
from app.user.models import User
from fastapi_jwt_auth import AuthJWT


from pydantic import BaseModel


class Settings(BaseModel):
    """https://indominusbyte.github.io/fastapi-jwt-auth/"""
    authjwt_secret_key: str = "secret"


class JWTAuth(AuthJWT):
    def get_current_user(self) -> Optional[User]:
        email = self.get_jwt_subject()
        user = get_user_by_email(email=email)
        return user


@JWTAuth.load_config
def get_config():
    return Settings()
