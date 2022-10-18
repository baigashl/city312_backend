from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer, PartnerRegisterSerializer, PartnerSerializer, PartnerUpdateSerializer
from apps.users.models import Partner


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

