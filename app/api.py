from fastapi import APIRouter

from app.auth.endpoints import router as auth_router
from app.user.endpoints import router as user_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
