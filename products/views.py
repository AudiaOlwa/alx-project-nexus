from django.shortcuts import render
# API logic for listing, creating, updating, deleting products
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    # select_related improves SQL performance by joining category table
    queryset = Product.objects.filter(is_active=True).select_related("category")
    serializer_class = ProductSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ["category__id", "category__slug"]  # For category filtering
    search_fields = ["title", "description"]  # For product search
    ordering_fields = ["price", "created_at"]  # For sorting output

