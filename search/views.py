
import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from jobs.document import UserDocument, SkillsDocument, JobDetailDocument, CategoryDocument

from jobs.serializers import SkillSerializer, JobDetailSerializer, CategorySerializer
# from blog.documents import ArticleDocument, UserDocument, CategoryDocument
# from blog.serializers import ArticleSerializer, UserSerializer, CategorySerializer
from authentication.serializers import UserRegistrationSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


# views


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class =UserRegistrationSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                    should=[
                        Q('match', username=query),
                        Q('match', first_name=query),
                        Q('match', last_name=query),
                    ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    
    def generate_q_expression(self, query):

        return Q(
                'multi_match', query=query,
                fields=[
                    'position',
                    'location',
                ], fuzziness='auto')


class SearchJobDetail(PaginatedElasticSearchAPIView):
    serializer_class = JobDetailSerializer
    document_class = JobDetailDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'job_title',
                    'job_detail',
                    'job_level',
                    
                ], fuzziness='auto')









# from django.core.paginator import Paginator
# from django.shortcuts import render
# # from django_elasticsearch_dsl.search import MultiSearch
# # from django_elasticsearch_dsl_drf.constants import (
# #     FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX_SIZE
# # )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from authentication.serializers import UserRegistrationSerializer




# class PaginatedDocumentViewSet(DocumentViewSet):

#     pagination_class = None

#     def get_paginated_response(self, data):
#         page = self.paginate_queryset(data)
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         paginator = Paginator(queryset, self.get_pagination_page_size())

#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         results = page_obj.object_list

#         serializer = self.get_serializer(results, many=True)
#         return self.get_paginated_response(serializer.data)


# class UserDocumentView(PaginatedDocumentViewSet):

#     document = UserDocument
#     serializer_class = UserRegistrationSerializer

# class SkillsDocumentView(PaginatedDocumentViewSet):

#     document = SkillsDocument
#     serializer_class = SkillSerializer


# class JobDetailDocumentView(PaginatedDocumentViewSet):

#     document = JobDetailDocument
#     serializer_class = JobDetailSerializer


# class CategoryDocumentView(PaginatedDocumentViewSet):

#     document = CategoryDocument
#     serializer_class = CategorySerializer