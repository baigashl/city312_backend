import requests
import jwt
from rest_framework.decorators import api_view
from rest_framework_simplejwt import exceptions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from city312_backend.settings import SECRET_KEY, DRF_RECAPTCHA_SECRET_KEY
from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)
from apps.users.serializers import (
    RegisterUserSerializer,
    ClientProfileSerializer,
    PartnerProfileSerializer,
    LoginUserSerializer,
)


@api_view(['POST', 'GET'])
def recaptcha(request):
    if request.method == 'POST':
        r = requests.post(
          'https://www.google.com/recaptcha/api/siteverify',
          data={
            'secret': DRF_RECAPTCHA_SECRET_KEY,
            'response': request.data['captcha_value'],
          }
        )
        return Response({'captcha': r.json()})
    return Response('gfjg')


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


class ClientRegisterView(CreateAPIView):
    serializer_class = ClientProfileSerializer
    queryset = ClientProfile.objects.all()


class PartnerRegisterView(CreateAPIView):
    serializer_class = PartnerProfileSerializer
    queryset = PartnerProfile.objects.all()


class LoginView(CreateAPIView):
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


