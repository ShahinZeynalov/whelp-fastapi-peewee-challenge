from typing import Any, Dict, Optional, Union

from app.user.models import User
from app.user.crud import get_user_by_email


def authenticate(email: str, password: str) -> Optional[User]:
    user = get_user_by_email(email=email)
    if not user:
        return None
    if not user.check_password(password):
        return None
    return user
