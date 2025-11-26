from django.db import models
from categories.models import Category
# Create your models here.
# Represents a product sold on the e-commerce platform

class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)  # Indexed for fast search
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)  # Indexed for sorting
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",
        on_delete=models.CASCADE,
        db_index=True
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # Default ordering by newest product first
        indexes = [
            # Composite index to speed up category filtering
            models.Index(fields=["category", "is_active"], name="product_category_active_idx"),
        ]

    def __str__(self):
        return self.title