from django.shortcuts import render
# API logic for listing, creating, updating, deleting products
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema,extend_schema_view, OpenApiExample


# Create your views here.

# ---------------------------------------------------------
# Swagger Documentation for Product API
# ---------------------------------------------------------
@extend_schema_view(
    list=extend_schema(
        summary="List all active products",
        description=(
            "Returns a paginated list of active products. "
            "Supports filtering by category, searching by title/description, "
            "and ordering by price or creation date."
        ),
        responses={200: ProductSerializer(many=True)},
        examples=[
            OpenApiExample(
                "Product List Example",
                value={
                    "count": 1,
                    "results": [
                        {
                            "id": 1,
                            "title": "Book ABC",
                            "slug": "book-abc",
                            "description": "A thriller novel",
                            "price": "9.99",
                            "category": {"id": 1, "name": "Books", "slug": "books"},
                            "stock": 10,
                            "is_active": True,
                            "created_at": "2025-01-01T12:00:00Z"
                        }
                    ]
                }
            )
        ],
    ),

    create=extend_schema(
        summary="Create a new product",
        description="Creates a product with category id. The slug is generated automatically.",
        request=ProductSerializer,
        responses={201: ProductSerializer},
        examples=[
            OpenApiExample(
                "Create Product Example",
                value={
                    "title": "Laptop Lenovo",
                    "description": "High performance laptop",
                    "price": "799.99",
                    "category": 2,
                    "stock": 5,
                    "is_active": True
                }
            )
        ],
    ),
)
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, creating, updating, and deleting products.
    Automatically documented with Swagger via drf-spectacular.
    """

    # Improve SQL performance by joining category table
    queryset = Product.objects.filter(is_active=True).select_related("category")
    serializer_class = ProductSerializer

    # Enable filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ["category__id", "category__slug"]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]