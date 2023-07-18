from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from jobs.document import JobDocument
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from  profiles.models import Profile

from profiles.serializers import ProfileSerializer
# Create your views here.

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "profile  created successfully",
            "status": status.HTTP_201_CREATED,
            "profile": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "profile deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "profile": None
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)