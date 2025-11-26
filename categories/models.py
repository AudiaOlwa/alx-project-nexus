from django.db import models
from django.utils.text import slugify
# Create your models here.
# Represents a logical grouping for products (e.g., Electronics, Books)

class Category(models.Model):
    # Index added because "name" is frequently used for lookups, filtering
    # and admin search. This improves query performance.
    name = models.CharField(max_length=100, unique=True, db_index=True) # Explicit index for faster filtering
    # Slug is unique → Django automatically creates an index.
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
