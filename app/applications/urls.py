from django.urls import path

from .views import (
JobApplicationListCreateView,
JobApplicationRetrieveUpdateDestroyView
)

urlpatterns = [
path('job-applications/', JobApplicationListCreateView.as_view(), name='job-application-list'),
path('job-applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), ),

]
