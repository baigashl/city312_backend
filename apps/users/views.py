from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer, UserRegisterSerializer, UserSerializer, UserUpdateSerializer, \
    PartnerSerializer, PartnerRegisterSerializer, PartnerUpdateSerializer, AdminSerializer
from .models import User, Partner
from rest_framework.schemas.openapi import AutoSchema
from ..discount.serializers import DiscountSerializer


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


class UserDetailUpdateDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
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

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = UserUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class PartnerRegisterView(CreateAPIView):
    queryset = Partner.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = PartnerRegisterSerializer


class PartnerListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def get(self, request, format=None):
        snippets = Partner.objects.all()
        serializer = PartnerSerializer(snippets, many=True)
        return Response(serializer.data)


class PartnerDetailUpdateDeleteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return Partner.objects.get(id=id)
        except Partner.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = PartnerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = PartnerUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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




