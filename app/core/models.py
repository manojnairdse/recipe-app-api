"""
Database Models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class USerManager(BaseUserManager):
    """Create Save and return new user"""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """USer in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_anonymous = models.BooleanField(default=False)
    # is_authenticated = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = USerManager()

    USERNAME_FIELD = "email"