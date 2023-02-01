import requests
from django.http import Http404
import jwt
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer, UserRegisterSerializer, UserSerializer, UserUpdateSerializer, \
    PartnerSerializer, PartnerRegisterSerializer, AdminSerializer
from .models import User, Partner
from rest_framework.schemas.openapi import AutoSchema
from ..discount.serializers import DiscountSerializer
from city312_backend.settings import SECRET_KEY, DRF_RECAPTCHA_SECRET_KEY


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



class CheckEmailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    schema = AutoSchema(
        tags=['AUTH'],
        component_name='Assign To Me',
        operation_id_base='CandidateAssignToMeList',
    )

    def post(self, request, format=None):
        if User.objects.filter(email=request.data['email'].lower()).exists():
            return Response('email already exists', status=status.HTTP_400_BAD_REQUEST)
        return Response('OK', status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer
    schema = AutoSchema(
        tags=['AUTH'],
        component_name='Assign To Me',
        operation_id_base='CandidateAssignToMeList',
    )

########################################################### USERS


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = UserRegisterSerializer


class UserListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)


class UserProfileUpdateDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, token):
        try:
            user = decode_auth_token(token)
            return User.objects.get(id=user['user_id'])
        except User.DoesNotExist:
            raise Http404

    def get(self, request, token, format=None):
        snippet = self.get_object(token)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, token, format=None):
        snippet = self.get_object(token)
        serializer = UserUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, token, format=None):
        snippet = self.get_object(token)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailAPIView(APIView):
    permission_classes = [AnonPermissionOnly]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)


#########################################Following
class UserAddFollowingAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def patch(self, request, format=None):
        snippet = self.get_object(id)
        print('follow', snippet.following)
        serializer = UserUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            snippet.following.add()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


############################################################# PARTNERS


class PartnerLoginView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class PartnerRegisterView(APIView):
    permission_classes = (AnonPermissionOnly,)
    # authentication_classes = []
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, request):
        serializer = PartnerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if 'logo' in list(request.data.keys()):
                file = request.FILES
                logo = file['logo']
            else:
                logo = None

            if 'banner' in list(request.data.keys()):
                file = request.FILES
                banner = file['banner']
            else:
                banner = None

            if 'phone2' in list(request.data.keys()):
                phone2 = request.data['phone2']
            else:
                phone2 = None

            if 'phone3' in list(request.data.keys()):
                phone3 = request.data['phone3']
            else:
                phone3 = None

            if 'phone4' in list(request.data.keys()):
                phone4 = request.data['phone4']
            else:
                phone4 = None

            user = Partner.objects.create(
                email=request.data['email'],
                activity_type=request.data['activity_type'],
                brand_name=request.data['brand_name'],
                organization_form=request.data['organization_form'],
                description=request.data['description'],
                inn=request.data['inn'],
                isPartner=True,
                logo=logo,
                banner=banner,
                phone1=request.data['phone1'],
                phone2=phone2,
                phone3=phone3,
                phone4=phone4,
                whatsapp=request.data['whatsapp'],
                youtube=request.data['youtube'],
                telegram=request.data['telegram'],
                facebook=request.data['facebook'],
                schedule=request.data['schedule'],
                start=request.data['start'],
                end=request.data['end']
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartnerListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = Partner.objects.all()
        serializer = PartnerSerializer(snippets, many=True)
        return Response(serializer.data)


class PartnerProfileUpdateDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, token):
        try:
            user = decode_auth_token(token)
            print(user['user_id'])
            return Partner.objects.get(id=user['user_id'])
        except Partner.DoesNotExist:
            raise Http404

    def get(self, request, token, format=None):
        partner = self.get_object(token)
        serializer1 = PartnerSerializer(partner)
        return Response(serializer1.data, status=status.HTTP_200_OK)

    def put(self, request, token, format=None):
        partner = self.get_object(token)
        serializer1 = PartnerSerializer(partner, request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_200_OK)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, token, format=None):
        snippet = self.get_object(token)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PartnerDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return Partner.objects.get(id=id)
        except Partner.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        partner = self.get_object(id)
        serializer1 = PartnerSerializer(partner)
        return Response(serializer1.data, status=status.HTTP_200_OK)


###############################################################################Admin

class AdminRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




