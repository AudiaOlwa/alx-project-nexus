from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Extends Django's default user model for possible future customization

class User(AbstractUser):
    # Additional user fields can be added here in the future
    pass
