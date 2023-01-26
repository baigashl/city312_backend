from django.urls import path
from .views import (
    DiscountListAPIView,
    DiscountCreateAPIView,
    FavoriteListAPIView,
    FavoriteCreateAPIView,
    GetUserFavoriteAPIView,
    FavoriteDetailAPIView,
    DiscountDetailAPIView,
    DiscountUpdateAPIView,
    DiscountDeleteAPIView,
    DiscountFilterListView,
)

urlpatterns = [
    path('', DiscountListAPIView.as_view(), name='discount-list'),
    path('create/', DiscountCreateAPIView.as_view(), name='discount-create'),
    path('<int:id>/deatil/', DiscountDetailAPIView.as_view(), name='discount-detail'),
    path('<int:id>/update/', DiscountUpdateAPIView.as_view(), name='discount-update'),
    path('<int:id>/delete/', DiscountDeleteAPIView.as_view(), name='discount-delete'),
    path('filter/', DiscountFilterListView.as_view(), name='discount-filter'),

    path('favorite/<int:user_id>/', GetUserFavoriteAPIView.as_view(), name='user-favorite'),
    path('favorite/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorite/create/', FavoriteCreateAPIView.as_view(), name='favorite-create'),
    path('favorite/detail/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='favorite-detail'),

    path('addtofavorite/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='add-to-favorite'),
]
