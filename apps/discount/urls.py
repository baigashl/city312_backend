from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    # DiscountListView,
    # DiscountCreateView,
    # DiscountDetailUpdateDeleteView,
    # GetUserFavoriteAPIView,
    # FavoriteDetailAPIView,
    DiscountViewSet,
    CommentView,
    # DiscountDetailAPIView,
    # DiscountUpdateAPIView,
    # DiscountDeleteAPIView,
    # DiscountFilterListView,
)

router = DefaultRouter()
router.register(r'discounts', DiscountViewSet, basename='discounts')
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    # path('', DiscountListView.as_view(), name='discount-list'),
    # path('create/', DiscountCreateView.as_view(), name='discount-create'),
    # path('<int:id>/update/', DiscountDetailUpdateDeleteView.as_view(), name='discount-detail'),
    # path('<int:id>/deatil/', DiscountDetailAPIView.as_view(), name='discount-detail'),
    # path('<int:id>/update/', DiscountUpdateAPIView.as_view(), name='discount-update'),
    # path('<int:id>/delete/', DiscountDeleteAPIView.as_view(), name='discount-delete'),
    # path('filter/', DiscountFilterListView.as_view(), name='discount-filter'),

    # path('favorite/<int:user_id>/', GetUserFavoriteAPIView.as_view(), name='user-favorite'),
    # path('favorite/', FavoriteListAPIView.as_view(), name='favorite-list'),
    # path('favorite/create/', FavoriteCreateAPIView.as_view(), name='favorite-create'),
    # path('favorite/detail/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='favorite-detail'),
    #
    # path('addtofavorite/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='add-to-favorite'),
]
