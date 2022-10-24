from django.urls import path
from .views import (
    DiscountListAPIView,
    DiscountCreateAPIView,
)

urlpatterns = [
    path('', DiscountListAPIView.as_view(), name='discount-list'),
    path('create/', DiscountCreateAPIView.as_view(), name='discount-create'),
]
