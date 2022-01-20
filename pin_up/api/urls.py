from django.urls import path
from .views import PinView

urlpatterns = [
    path('pins', PinView.as_view())
]