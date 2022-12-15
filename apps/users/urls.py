from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import (
    LoginView,
    UserRegisterView,
    UserListAPIView,
    UserDetailUpdateDeleteAPIView,
    PartnerRegisterView,
    PartnerListAPIView,
    PartnerDetailUpdateDeleteAPIView,
    CheckEmailAPIView,
    UserAddFollowingAPIView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterView.as_view(), name='register-user'),
    path('partner/register/', PartnerRegisterView.as_view(), name='register-partner'),

    path('check-email', CheckEmailAPIView.as_view(), name='check-email'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('partner/', PartnerListAPIView.as_view(), name='partner-list'),
    path('<int:id>/', UserDetailUpdateDeleteAPIView.as_view(), name='user-detail'),
    path('partner/<int:id>/', PartnerDetailUpdateDeleteAPIView.as_view(), name='partner-detail'),

    path('follow/<int:id>/', UserAddFollowingAPIView.as_view(), name='follow'),
]
