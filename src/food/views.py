from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import FoodSerializer
from .models import Food
# Create your views here.


class FoodDataListAPIView(ListAPIView):
    serializer_class = FoodSerializer
    pagination_classes = [LimitOffsetPagination]
    queryset = Food.objects.all()
