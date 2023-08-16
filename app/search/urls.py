from django.urls import path

from .views import (
    SearchCategories,
    SearchJobDetail,
    SearchUsers

)

urlpatterns = [
    path('category/<str:query>/', SearchCategories.as_view()),
    path('jobsDetails/<str:query>/', SearchJobDetail.as_view()),
    path('user/<str:query>/', SearchUsers.as_view()),


]
