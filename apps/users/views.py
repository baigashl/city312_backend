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
    PartnerSerializer, PartnerRegisterSerializer, PartnerUpdateSerializer, FavoriteSerializer
from .models import User, Partner, Favorite
from ..discount.serializers import DiscountSerializer


class CheckEmailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []

    def post(self, request, format=None):
        if User.objects.filter(email=request.data['email'].lower()).exists():
            return Response('email already exists', status=status.HTTP_400_BAD_REQUEST)
        return Response('OK', status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer

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


class UserDetailAPIView(APIView):
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


##################################################################### Favorites


class GetUserFavoriteAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        snippet = Favorite.objects.get(user_id=user_id)
        discounts = snippet.discount.all()
        print('asdasdasd', discounts)
        serializer = FavoriteSerializer(snippet)
        serializer2 = DiscountSerializer(discounts, many=True)
        data = serializer.data
        data['discount'] = serializer2.data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        snippet = Favorite.objects.get(user_id=user_id)
        serializer = FavoriteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        activity_type = Favorite.objects.all()
        serializers = FavoriteSerializer(activity_type, many=True)
        return Response(serializers.data)


class FavoriteCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = FavoriteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, user_id):
        try:
            return Favorite.objects.get(user_id=user_id)
        except Favorite.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        serializer = FavoriteSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        serializer = FavoriteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


