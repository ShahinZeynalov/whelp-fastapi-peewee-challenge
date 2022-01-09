from pydantic import BaseModel


class LoginRequestSchema(BaseModel):
    email: str
    password: str
