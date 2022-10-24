from django.urls import path
from .views import (ActivityTypeListAPIView,
                    ActivityTypeDetailAPIView,
                    ActivityTypeCreateAPIView,
                    CategoryListAPIView,
                    CategoryDetailAPIView)


urlpatterns = [path('list/', ActivityTypeListAPIView.as_view(), name='activity_type_list'),
               path('create/', ActivityTypeCreateAPIView.as_view(), name='activity_type_create'),
               path('detail/<int:id>', ActivityTypeDetailAPIView.as_view(), name='activity_type_detail'),
               ]