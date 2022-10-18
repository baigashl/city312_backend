from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import (
    UserLoginView,
    UserRegisterView,
    UserListAPIView,
    UserDetailAPIView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login-partner'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterView.as_view(), name='register-partner'),

    path('', UserListAPIView.as_view(), name='partner-list'),
    path('<int:id>/', UserDetailAPIView.as_view(), name='detail'),
]