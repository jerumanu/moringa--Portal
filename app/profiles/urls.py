from django.urls import path

from .views import (
ProfileRetrieveUpdateDestroyAPIView,
ProfileListCreateAPIView, 
)

urlpatterns = [
    path('profile', ProfileListCreateAPIView.as_view(), name='child-list'),
    path('profile/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='child-detail'),


]
