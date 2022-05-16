from .views import CustomAuthToken
from django.urls import path, include

urlpatterns = [
    path('obtain-token/', CustomAuthToken.as_view()),
]
