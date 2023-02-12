import jwt
from django.contrib.sites import requests
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)
from apps.users.serializers import (
    ClientProfileSerializer,
    PartnerProfileSerializer,
    LoginUserSerializer,
    UserSerializer,
)
from apps.users.permissions import (
    IsClient,
    IsPartner,
)
from city312_backend import settings
from city312_backend.settings import SECRET_KEY


def decode_auth_token(token):
    try:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        msg = 'Signature has expired. Login again.'
        raise exceptions.AuthenticationFailed(msg)
    except jwt.DecodeError:
        msg = 'Error decoding signature. Type valid token'
        raise exceptions.AuthenticationFailed(msg)
    except jwt.InvalidTokenError:
        raise exceptions.AuthenticationFailed()
    return user


class RegisterClientView(CreateAPIView):
    """Register client view"""

    serializer_class = ClientProfileSerializer
    queryset = User.objects.all()


class RegisterPartnerView(CreateAPIView):
    """Register partner view"""

    serializer_class = PartnerProfileSerializer
    queryset = User.objects.all()


class LoginView(CreateAPIView):
    """All user login view """

    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("Пользователь с такими учетными данными не найден!")
        if not user.check_password(password):
            raise AuthenticationFailed("Неверный пароль!")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class UserProfileView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin):

    def get_serializer_class(self):
        """Filtering serializer by user_type"""

        user = self.request.user
        if user.user_type == 'Клиент':
            return ClientProfileSerializer
        elif user.user_type == 'Партнер':
            return PartnerProfileSerializer

    permission_classes = (IsClient | IsPartner,)
    serializer_class = get_serializer_class
    queryset = User.objects.all()

    def get_queryset(self):
        """Filtering queryset by user_type"""

        user = self.request.user
        if user.user_type == 'Клиент':
            queryset = ClientProfile.objects.all()
            return queryset.filter(user=user)
        elif user.user_type == 'Партнер':
            queryset = PartnerProfile.objects.all()
            return queryset.filter(user=user)

    def update(self, request, *args, **kwargs):
        """Updating partner profile data and password"""

        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            if instance.user:
                instance.user.set_password(instance.user.password)
                instance.user.save()
            return Response(serializer.data)
        return Response(serializer.errors)