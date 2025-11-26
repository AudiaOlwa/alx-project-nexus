from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.generics import ListAPIView
from drf_spectacular.utils import extend_schema, OpenApiExample

# Create your views here.

#Swagger Documentation for Category API
# ---------------------------------------------------------------------
# CATEGORY LIST ENDPOINT
# ---------------------------------------------------------------------

@extend_schema(
    summary="List all categories",
    description="Returns a list of all product categories available in the store.",
    responses={200: CategorySerializer(many=True)},
    examples=[
        OpenApiExample(
            "Categories Example",
            value=[
                {"id": 1, "name": "Books", "slug": "books"},
                {"id": 2, "name": "Electronics", "slug": "electronics"},
            ]
        )
    ],
)
class CategoryList(ListAPIView):
    """
    API endpoint to return the list of all categories.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()