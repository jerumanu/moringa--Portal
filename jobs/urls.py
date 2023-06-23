from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from  .views import (

    CategoriesListCreateAPIView,
    CategoriesRetrieveUpdateDestroyAPIView,
    CategoryRestoreView,
    CategorySoftDeleteView,
    JobApplicationListCreateView,
    JobDetailsListCreateAPIView,
    JobDetailsRetrieveUpdateDestroyAPIView,
    SkillsListCreateAPIView,
    SkillsRetrieveUpdateDestroyAPIView,
    ResponsibilitiesListCreateAPIView,
    ResponsibilitiesRetrieveUpdateDestroyAPIView,
    QualificationsListCreateAPIView,
    QualificationsRetrieveUpdateDestroyAPIView,
    JobApplicationRetrieveUpdateDestroyView,

    )


urlpatterns = [
    
    path('categories', CategoriesListCreateAPIView.as_view(),),
    path('job-applications/', JobApplicationListCreateView.as_view(), name='job-application-list'),
    path('job-applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), ),

    path('categories/<int:pk>/', CategoriesRetrieveUpdateDestroyAPIView.as_view(), ),
    path('jobDetail', JobDetailsListCreateAPIView.as_view(), name='child-list'),
    path('jobDetail/<int:pk>/', JobDetailsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('skills/', SkillsListCreateAPIView.as_view(), name='child-list'),
    path('skills/<int:pk>/', SkillsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('responsibilities', ResponsibilitiesListCreateAPIView.as_view(), name='child-list'),
    path('responsibilities/<int:pk>/', ResponsibilitiesRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('qualifications', QualificationsListCreateAPIView.as_view(), name='child-list'),
    path('qualifications/<int:pk>/', QualificationsRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),
    path('category/<int:pk>/soft-delete/', CategorySoftDeleteView.as_view(), name='category-soft-delete'),
    path('category/<int:pk>/restore/', CategoryRestoreView.as_view(), name='category-restore')


]