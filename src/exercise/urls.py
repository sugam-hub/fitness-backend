from django.urls import path, include
from .views import ExerciseDataListAPIView
urlpatterns = [
    path("list/", ExerciseDataListAPIView.as_view(),
         name="ExerciseDetailListView")

]
