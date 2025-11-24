# Converts Product objects to/from JSON for API communication
from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    # Read-only nested category
    category = CategorySerializer(read_only=True)

    # Used for write operations (POST/PUT)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Product._meta.get_field("category").remote_field.model.objects.all(),
        write_only=True,
        source="category"
    )

    class Meta:
        model = Product
        fields = [
            "id","title","slug","description","price",
            "category","category_id","stock",
            "is_active","created_at"
        ]
