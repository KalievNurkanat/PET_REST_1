from django.contrib.auth.models import BaseUserManager
import re

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not phone_number:
            raise ValueError("Telephone is required")
        if not username:
            raise ValueError("Name is required")
        if not password:
            raise ValueError("Password is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone_number=phone_number, password=password, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, email, phone_number, password, **extra_fields):
      extra_fields.setdefault("is_staff", True)
      extra_fields.setdefault("is_superuser", True)
      extra_fields.setdefault("is_active", True)
      
      if not username:
          raise ValueError("Enter ur name")
      if not re.match(r'^\+996\d{9}$', phone_number):
          raise ValueError("Enter ur num correctly with 9 digits after +996")
      if not email:
          raise ValueError("Enter ur email")
      if extra_fields.get("is_active") is not True:
          raise ValueError("superuser must be active")
      
      if extra_fields.get("is_staff") is not True:
          raise ValueError("superuser must be staff")
      
      if extra_fields.get("is_superuser") is not True:
          raise ValueError("superuser must be superuser")
      
      return self.create_user(username, email, phone_number, password, **extra_fields)
      