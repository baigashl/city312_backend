from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import (
    PartnerLoginView,
    PartnerRegisterView,
    PartnerListAPIView,
    PartnerDetailAPIView,
)

urlpatterns = [
    path('', PartnerListAPIView.as_view(), name='partner-list'),
    path('<int:id>/', PartnerDetailAPIView.as_view(), name='detail'),
    path('login/', PartnerLoginView.as_view(), name='login-partner'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', PartnerRegisterView.as_view(), name='register-partner'),
]