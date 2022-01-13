from django.urls import path
from .views import PinView

urlpatterns = [
    path('pins', views.PinView.as_view())
]