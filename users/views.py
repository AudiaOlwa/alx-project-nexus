from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Create your views here.
# View responsible for user registration


# ---------------------------------------------------------------------
# USER REGISTRATION
# ---------------------------------------------------------------------

@extend_schema(
    summary="Register a new user",
    description="Creates a new user account. Password is securely hashed.",
    request=RegisterSerializer,
    responses={
        201: RegisterSerializer,
        400: {"detail": "Validation errors"},
    },
    examples=[
        OpenApiExample(
            "User Registration Example",
            value={
                "username": "john_doe",
                "email": "john@example.com",
                "password": "password123"
            }
        )
    ],
)
class RegisterView(generics.CreateAPIView):
    """
    API endpoint for registering new users.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------------------------------------------------
# JWT LOGIN
# ---------------------------------------------------------------------

@extend_schema(
    summary="Authenticate user using username and password",
    description="Returns access & refresh tokens for authenticated users.",
    request=CustomTokenObtainPairSerializer,
    responses={200: CustomTokenObtainPairSerializer},
    examples=[
        OpenApiExample(
            "Login Example",
            value={"username": "john_doe", "password": "password123"}
        )
    ],
)
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    JWT Login Endpoint
    """
    serializer_class = CustomTokenObtainPairSerializer


# ---------------------------------------------------------------------
# JWT REFRESH TOKEN
# ---------------------------------------------------------------------

@extend_schema(
    summary="Refresh access token",
    description="Returns a new access token using a valid refresh token.",
)
class CustomTokenRefreshView(TokenRefreshView):
    """
    JWT Token Refresh Endpoint
    """
    pass