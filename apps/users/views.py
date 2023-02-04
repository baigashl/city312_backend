import requests
import jwt
from rest_framework.decorators import api_view
from rest_framework_simplejwt import exceptions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet

from city312_backend.settings import SECRET_KEY, DRF_RECAPTCHA_SECRET_KEY
from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)
from apps.users.serializers import (
    UserSerializer,
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


class ClientProfileView(ModelViewSet):
    """Client profile view"""

    serializer_class = ClientProfileSerializer
    queryset = ClientProfile.objects.all()

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


