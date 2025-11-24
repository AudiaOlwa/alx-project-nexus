from django.contrib import admin
from .models import Category

# Register your models here.
# Enables category management in Django admin

admin.site.register(Category)
