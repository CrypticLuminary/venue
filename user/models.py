from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region="NP")
    address = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email
