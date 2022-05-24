from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        print(self.request.user)
        profile = Profile.objects.get(
            user=self.request.user)
        print(profile)
        return profile

    def update(self, request, *args, **kwargs):
        data = request.data
        # data.pop("user")
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
