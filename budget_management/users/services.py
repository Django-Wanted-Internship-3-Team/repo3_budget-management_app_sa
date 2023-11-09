from django.db import transaction

from budget_management.common.exceptions import ValidationError
from budget_management.users.models import User
from budget_management.users.selectors import get_user_by_username


class UserService:
    def validate_unique_usernmae(self, username: str):
        if username:
            username_exists = get_user_by_username(username)
            if username_exists:
                raise ValidationError("Username already exists.")

    def validate_password(self, password: str):
        if password:
            if len(password) < 8:
                raise ValidationError("Password must be at least 8 characters long.")

    @transaction.atomic
    def create(self, username: str, password: str) -> User:
        self.validate_unique_usernmae(username)
        self.validate_password(password)
        user = User.objects.create_user(username=username, password=password)
        return user
