from django.urls import path
from .views import (
    CartListAPIView,
    CartCreateAPIView,
    CartDetailAPIView,
)


urlpatterns = [
    path('', CartListAPIView.as_view(), name='cart-list'),
    path('create/', CartCreateAPIView.as_view(), name='cart-create'),
    path('<int:id>/', CartDetailAPIView.as_view(), name='cart-detail'),


]