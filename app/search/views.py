
import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from jobs.document import UserDocument, SkillsDocument, JobDetailDocument, CategoryDocument

from jobs.serializers import SkillSerializer, JobDetailSerializer, CategorySerializer
from authentication.serializers import   UserRegistrationSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        
        """This method should be overridden and return a Q() expression.
        """

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
                        Q('match',role=query),
                        Q('match', first_name=query),
                        Q('match', last_name=query),
                    ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument
    
    def generate_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=['title', 'position', 'location'],
            fuzziness='auto'
        )


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
    









