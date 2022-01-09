from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from app.core import security
from app.core.config import settings
from . import database
from app.user.models import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


async def reset_db_state():
    database.db._state._state.set(database.db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()

def get_current_user(
    Authorize: AuthJWT = Depends()
) -> User:
    Authorize.jwt_required()

    subject = Authorize.get_jwt_subject()
    user = User.filter(email=subject).first()
    import pdb
    pdb.set_trace()

    return user
