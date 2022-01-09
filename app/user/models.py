import peewee

from app.core.database import BaseModel
from app.core.security import get_password_hash
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    email = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    def set_password(self, password):
        self.password = get_password_hash(password)
        return self.password

    def check_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)
