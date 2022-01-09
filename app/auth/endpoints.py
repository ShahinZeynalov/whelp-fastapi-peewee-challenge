from fastapi import APIRouter, Body, Depends, HTTPException, Request
from app.core import dependencies
from app.user.schemas import UserSchema, UserCreateSchema
from app.user.crud import (
    get_user_by_email, create_user
)
from .jwt_auth import JWTAuth
from .schemas import LoginRequestSchema
from .services import authenticate


router = APIRouter()


@router.post('/login')
def login(form_data: LoginRequestSchema = Depends(), Authorize: JWTAuth = Depends()):
    user = authenticate(form_data.email, form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)
    return {"access_token": access_token, "refresh_token": refresh_token, "type": 'Bearer'}


@router.post("/signup", response_model=UserSchema, dependencies=[Depends(dependencies.get_db)])
def signup(user: UserCreateSchema):
    db_user = get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user=user)


@router.post('/refresh', dependencies=[Depends(dependencies.get_db)])
def refresh(Authorize: JWTAuth = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    subject = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=subject)
    return {"access_token": new_access_token}
