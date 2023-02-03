from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from apps.users.views import (
    LoginView,
    ClientRegisterView,
    PartnerRegisterView,
    recaptcha
)

urlpatterns = [
    path('recaptcha/', recaptcha, name='recaptcha'),
    path('login/', LoginView.as_view(), name='login'),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/client/', ClientRegisterView.as_view(), name='register-client'),
    path('register/partner/', PartnerRegisterView.as_view(), name='register-partner'),
]
