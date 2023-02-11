import jwt
from django.contrib.sites import requests
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
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


class ClientProfileView(ModelViewSet):
    """Client profile view"""

    serializer_class = ClientProfileSerializer
    queryset = ClientProfile.objects.all()

    # def create(self, request, *args, **kwargs):
    #     """Creating a new client profile"""
    #
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         recaptcha_response = request.data.get('captcha')
    #         response = requests.post(settings.DRF_RECAPTCHA_VERIFY_ENDPOINT,
    #                                  data={'recaptcha_response': recaptcha_response})
    #         if response.json().get('status') == 'success':
    #             self.perform_create(serializer)
    #             headers = self.get_success_headers(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #         else:
    #             return Response({'error': 'reCAPTCHA verification failed'}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Updating client profile data and password"""

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


class PartnerProfileView(ModelViewSet):
    """Partner profile view"""

    serializer_class = PartnerProfileSerializer
    queryset = PartnerProfile.objects.all()

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
                "status": "Вы, успешно авторизовались!",
                "user_id": str(user.id),
                "user_type": str(user.user_type),
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
