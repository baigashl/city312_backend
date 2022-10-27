from django.urls import path
from .views import (
    CartListAPIView,
    CartCreateAPIView,
    CartDetailAPIView,
    GetUserCartAPIView,
)


urlpatterns = [
    path('user_cart/<int:user_id>', GetUserCartAPIView.as_view(), name='user-cart'),
    path('', CartListAPIView.as_view(), name='cart-list'),
    path('create/', CartCreateAPIView.as_view(), name='cart-create'),
    path('<int:id>/', CartDetailAPIView.as_view(), name='cart-detail'),


]