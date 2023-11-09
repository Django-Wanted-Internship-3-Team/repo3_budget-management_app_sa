from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from budget_management.common.models import BaseModel
from budget_management.users.managers import UserManager


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects: models.Manager = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
