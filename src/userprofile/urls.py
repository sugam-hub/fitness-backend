from django.urls import path, include
from .views import ProfileRetrieveUpdateAPIView
urlpatterns = [
    path("", ProfileRetrieveUpdateAPIView.as_view(),
         name="ProfileRetrieveAPIView")

]
