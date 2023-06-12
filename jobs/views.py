from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from jobs.document import JobDocument
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
 
from jobs.models import Category,JobDetail,Skill,Responsibility,Qualification
from jobs.serializes import CategorySerializer,JobDetailSerializer,SkillSerializer,ResponsibilitySerializer,QualificationSerializer
from rest_framework import generics


class JobDocumentView(DocumentViewSet):
    document = JobDocument
    serializer_class = CategorySerializer
    pagination_class = None  # Remove pagination for simplicity

    def get_queryset(self):
        return self.document.search().query("match_all")  # Return all documents

class JobSearchAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = None  # Remove pagination for simplicity

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Get search query from URL parameter 'q'
        if query:
            return JobDocument.search().query("multi_match", query=query, fields=['title', 'job_categories.job_title'])
        else:
            return JobDocument.search().query("match_all")

class CategorySearchAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer
    
    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)
        if search_query:
            category_index = CategoryIndex()
            response = category_index.search(search_query)
            positions = [hit.position for hit in response.hits]
            queryset = Category.objects.filter(position__in=positions)
        else:
            queryset = Category.objects.none()
        return queryset


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
