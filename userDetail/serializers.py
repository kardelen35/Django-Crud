from rest_framework import serializers
from .models import User

# Serializers help us convert our complex data into a format that can be easily sent over the internet.

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'