from typing import Optional

from budget_management.users.models import User


def get_user_by_username(username: str) -> Optional[User]:
    return User.objects.filter(username=username).first()
