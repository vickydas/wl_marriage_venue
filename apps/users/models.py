from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role="USER", **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, role="SUPERADMIN", password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("USER", "User"),
        ("ADMIN", "Admin"),
        ("SUPERADMIN", "Super Admin"),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="USER")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(upload_to='users/profile_images/', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email