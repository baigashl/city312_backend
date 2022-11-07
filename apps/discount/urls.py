from django.urls import path
from .views import (
    DiscountListAPIView,
    DiscountCreateAPIView,
    FavoriteListAPIView,
    FavoriteCreateAPIView,
    GetUserFavoriteAPIView,
    FavoriteDetailAPIView,
)

urlpatterns = [
    path('', DiscountListAPIView.as_view(), name='discount-list'),
    path('create/', DiscountCreateAPIView.as_view(), name='discount-create'),

    path('favorite/<int:user_id>/', GetUserFavoriteAPIView.as_view(), name='user-favorite'),
    path('favorite/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorite/create/', FavoriteCreateAPIView.as_view(), name='favorite-create'),
    path('favorite/detail/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='favorite-detail'),
]
