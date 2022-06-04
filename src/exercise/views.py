from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ExerciseSerializer
from .models import Exercise
# Create your views here.


class ExerciseDataListAPIView(ListAPIView):
    serializer_class = ExerciseSerializer
    pagination_classes = [LimitOffsetPagination]
    # queryset = Exercise.objects.all()

    def get_queryset(self):
        bmi = self.request.GET.get("bmi_affection_rate")
        ex = Exercise.objects.all()
        qs = ex
        if(bmi):
            bmi = float(bmi)
            if(bmi < 18.5):
                qs = ex.filter(bmi_affection_rate__gte=1)
            elif (bmi >= 18.5 and bmi < 25):
                qs = ex.filter(bmi_affection_rate=0)
            elif (bmi >= 25 and bmi < 30):
                qs = ex.filter(bmi_affection_rate__lt=0)
            elif (bmi >= 30):
                qs = ex.filter(bmi_affection_rate__lt=0)
        return qs
