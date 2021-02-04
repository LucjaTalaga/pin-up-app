from rest_framework import serializers
from .models import User, Pin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ('id', 'author', 'content')