from django.db import models
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    first_name = models.CharField(null=True, blank=True)
    last_name = models.CharField(null=True, blank=True)
    password = models.CharField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number", "password"]

    def __str__(self):
        return f"{self.username}"


class Confirm(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)