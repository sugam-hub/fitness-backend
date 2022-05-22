from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ExerciseSerializer
from .models import Exercise
# Create your views here.


class ExerciseDataListAPIView(ListAPIView):
    serializer_class = ExerciseSerializer
    pagination_classes = [LimitOffsetPagination]
    queryset = Exercise.objects.all()
