from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
# Create your views here.
# View responsible for user registration


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow registration without token
