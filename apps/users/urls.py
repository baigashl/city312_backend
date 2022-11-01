from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import (
    LoginView,
    UserRegisterView,
    UserListAPIView,
    UserDetailAPIView,
    PartnerRegisterView,
    PartnerListAPIView,
    PartnerDetailAPIView,
    CheckEmailAPIView,
    FavoriteListAPIView,
    FavoriteCreateAPIView,
    GetUserFavoriteAPIView,
    FavoriteDetailAPIView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterView.as_view(), name='register-user'),
    path('partner/register/', PartnerRegisterView.as_view(), name='register-partner'),

    path('check-email', CheckEmailAPIView.as_view(), name='check-email'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('partner/', PartnerListAPIView.as_view(), name='partner-list'),
    path('user/<int:id>/', UserDetailAPIView.as_view(), name='detail'),
    path('partner/<int:id>/', PartnerDetailAPIView.as_view(), name='detail'),

    path('favorite/<int:user_id>/', GetUserFavoriteAPIView.as_view(), name='user-favorite'),
    path('favorite/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorite/create/', FavoriteCreateAPIView.as_view(), name='favorite-create'),
    path('favorite/detail/<int:user_id>/', FavoriteDetailAPIView.as_view(), name='favorite-detail'),
]