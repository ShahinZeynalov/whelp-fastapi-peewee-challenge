
from .models import User
from .schemas import UserCreateSchema


def get_user(user_id: int) -> User:
    return User.filter(User.id == user_id).first()


def get_user_by_email(email: str) -> User:
    return User.filter(User.email == email).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(User.select().offset(skip).limit(limit))


def create_user(user: UserCreateSchema):
    db_user = User(email=user.email)
    db_user.set_password(user.password)
    db_user.save()
    return db_user
