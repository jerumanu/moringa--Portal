from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from jobs.document import JobDocument
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from jobs.models import Category,JobDetail,Skill,Responsibility,Qualification
from jobs.serializers import(
CategorySerializer,

JobDetailSerializer,
SkillSerializer,
ResponsibilitySerializer,
QualificationSerializer)

from rest_framework import generics



class CategorySoftDeleteView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, pk):
        category = get_object_or_404(self.get_queryset(), pk=pk)
        category.soft_delete()
        return Response({'message': 'Category soft-deleted successfully.'})
    

class CategoryRestoreView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, pk):
        category = self.get_object()
        category.restore()
        return Response({'message': 'Category restored successfully.'})

class CategoriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "category  created successfully",
            "status": status.HTTP_201_CREATED,
            "category": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class CategoriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "category deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "category": None
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)

class JobDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobDetail.objects.all()
    serializer_class = JobDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "Job details  created successfully",
            "status": status.HTTP_201_CREATED,
            "jobs_details": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class JobDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobDetail.objects.all()
    serializer_class = JobDetailSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "Job details deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "Job_detail": None
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
    
class SkillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "Skills created successfully",
            "status": status.HTTP_201_CREATED,
            "Skills": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class SkillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "Skills deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "Skills": None
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
class ResponsibilitiesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "Responsibilities  created successfully",
            "status": status.HTTP_201_CREATED,
            "Responsibilities": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class ResponsibilitiesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responsibility.objects.all()
    serializer_class = ResponsibilitySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "Responsibilities deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "Responsibilities": None
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
class QualificationsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Create the response
        response_data = {
            "message": "Qualifications created successfully",
            "status": status.HTTP_201_CREATED,
            "Qualifications": serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

class QualificationsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Create the response
        response_data = {
            "message": "Qualifications deleted successfully",
            "status": status.HTTP_204_NO_CONTENT,
            "Qualifications": None
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
