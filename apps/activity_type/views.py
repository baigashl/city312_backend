from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ActivityType, Category
from .serialisers import ActivityTypeSerializer, CategorySerializer


class CourseTypeListAPIView(APIView):
    # permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.JWTAuthentication]
    parser_classes = [JSONParser]

    def get(self, request):
        snippets = ActivityType.objects.all()
        serializer = ActivityTypeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseTypeDetailAPIView(APIView):
    permission_classes = [IsSubAdminPermission]
    # authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return CourseType.objects.get(id=id)
        except CourseType.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseTypeSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = CourseTypeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

