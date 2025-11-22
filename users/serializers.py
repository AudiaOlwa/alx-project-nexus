# Serializer used to validate and create new user accounts
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Prevent password from being exposed in response
    
    class Meta:
        model = User
        fields = ("id","username","email","password")

    
    def create(self, validated_data):
        # Use Django's built-in user creation to hash passwords properly
        user = User.objects.create_user(**validated_data)
        return user
