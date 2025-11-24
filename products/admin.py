from django.contrib import admin
from .models import Product

# Register your models here.
# Enables product management in Django admin
admin.site.register(Product)
