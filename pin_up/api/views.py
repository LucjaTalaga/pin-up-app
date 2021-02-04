from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, PinSerializer
from .models import User, Pin
# Create your views here.

class PinView(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
