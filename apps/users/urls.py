from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from apps.users.recaptcha_verify import verify_recaptcha
from apps.users.views import (
    LoginView,
    RegisterClientView,
    RegisterPartnerView,
    UserProfileView,
)

router = DefaultRouter()
router.register('profile', UserProfileView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/client/', RegisterClientView.as_view(), name='register_client'),
    path('register/partner/', RegisterPartnerView.as_view(), name='register_partner'),
    path('recaptcha/verify/', verify_recaptcha, name='verify_recaptcha'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
