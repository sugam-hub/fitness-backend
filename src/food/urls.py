from django.urls import path, include
from .views import FoodDataListAPIView
urlpatterns = [
    path("list/", FoodDataListAPIView.as_view(), name="FoodDetailListView")

]
