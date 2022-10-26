from django.urls import path
from .views import (
    ActivityTypeListAPIView,
    ActivityTypeDetailAPIView,
    ActivityTypeCreateAPIView,
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryDetailAPIView
)


urlpatterns = [
    path('list/', ActivityTypeListAPIView.as_view(), name='activity_type_list'),
    path('create/', ActivityTypeCreateAPIView.as_view(), name='activity_type_create'),
    path('detail/<int:id>', ActivityTypeDetailAPIView.as_view(), name='activity_type_detail'),


    path('cat_list/', CategoryListAPIView.as_view(), name='category_list'),
    path('cat_create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('cat_detail/<int:id>', CategoryDetailAPIView.as_view(), name='category_detail'),
]