# Exposes registration and JWT login endpoints
from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # POST: create user
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # POST: get access/refresh token
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # POST: refresh access token
]
