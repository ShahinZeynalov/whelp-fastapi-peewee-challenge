from typing import Any, List, Optional
from pydantic import BaseModel
from app.core.utils import PeeweeGetterDict


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
