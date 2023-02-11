from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

# from apps.users.recaptcha_verify import verify_recaptcha
from apps.users.views import (
    LoginView,
    ClientProfileView,
    PartnerProfileView
)

router = DefaultRouter()
router.register('register/client', ClientProfileView)
router.register('register/partner', PartnerProfileView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    # path('recaptcha/verify/', verify_recaptcha, name='verify_recaptcha'),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
