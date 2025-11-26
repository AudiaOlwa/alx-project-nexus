from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Extends Django's default user model for possible future customization

class User(AbstractUser):
    # Index added only if email is used for authentication.
    # This makes login and lookups significantly faster.
    email = models.EmailField(unique=True, db_index=True)
    # Additional user fields can be added here in the future
    pass
