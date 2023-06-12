from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from  .views import (

    CategoriesListCreateAPIView,
    CategoriesRetrieveUpdateDestroyAPIView,
    JobDetailsListCreateAPIView,
    JobDetailsRetrieveUpdateDestroyAPIView,
    JobSearchAPIView,
    SkillsListCreateAPIView,
    SkillsRetrieveUpdateDestroyAPIView,
    ResponsibilitiesListCreateAPIView,
    ResponsibilitiesRetrieveUpdateDestroyAPIView,
    QualificationsListCreateAPIView,
    QualificationsRetrieveUpdateDestroyAPIView,
    

    )


urlpatterns = [
    path('categories', CategoriesListCreateAPIView.as_view(),),
    path('search/', JobSearchAPIView.as_view(), name='job-search'),
    path('categories/<int:pk>/', CategoriesRetrieveUpdateDestroyAPIView.as_view(), ),
    path('jobDetail', JobDetailsListCreateAPIView.as_view(), name='child-list'),
    path('jobDetail/<int:pk>/', JobDetailsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('skills/', SkillsListCreateAPIView.as_view(), name='child-list'),
    path('skills/<int:pk>/', SkillsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('responsibilities', ResponsibilitiesListCreateAPIView.as_view(), name='child-list'),
    path('responsibilities/<int:pk>/', ResponsibilitiesRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('qualifications', QualificationsListCreateAPIView.as_view(), name='child-list'),
    path('qualifications/<int:pk>/', QualificationsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
]