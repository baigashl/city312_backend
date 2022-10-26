from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialisers import ActivityTypeSerializer, CategorySerializer
from .models import ActivityType, Category
from django.http import Http404
from rest_framework import status, permissions


class ActivityTypeListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        activity_type = ActivityType.objects.all()
        serializers = ActivityTypeSerializer(activity_type, many=True)
        return Response(serializers.data)


class ActivityTypeCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ActivityTypeSerializer

    def post(self, request):
        serializers = ActivityTypeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityTypeDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return ActivityType.objects.get(id=id)
        except ActivityType.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ActivityTypeSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ActivityTypeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class CategoryCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    serializer_class = CategorySerializer

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CategorySerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

