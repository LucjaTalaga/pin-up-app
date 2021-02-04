from django.urls import path
from . import views

urlpatterns = [
    path('pins', views.PinView.as_view())
]