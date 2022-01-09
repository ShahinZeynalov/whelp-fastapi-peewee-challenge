from fastapi import APIRouter, Depends
from app.core import dependencies
from app.user.schemas import UserSchema
from app.auth.jwt_auth import JWTAuth
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.post('/me', response_model=UserSchema, dependencies=[Depends(dependencies.get_db)])
def me(Authorize: JWTAuth = Depends()):
    Authorize.jwt_required()

    user = Authorize.get_current_user()

    return user
