from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Discount, DiscountType, Favorite
from .serializers import DiscountSerializer, DiscountTypeSerializer, FavoriteSerializer

from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'


class DiscountListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def get(self, request):
        snippets = Discount.objects.all()
        print(snippets.count())
        serializer = DiscountSerializer(snippets, many=True)
        page_num = int(self.request.query_params.get('page'))
        return Response({
            'count': snippets.count(),
            'success': True,
            'results': serializer.data[page_num*10-10:page_num*10],
        }, status=status.HTTP_200_OK)


# class DiscountListAPIView(APIView, CustomPagination):
#     permission_classes = [permissions.AllowAny]
#     # authentication_classes = []
#     parser_classes = [JSONParser]
#
#     def get(self, request):
#         snippets = Discount.objects.all()
#         print(snippets.count())
#         # serializer = DiscountSerializer(snippets, many=True)
#         page_number = self.request.query_params.get('page_number ', 1)
#         page_size = self.request.query_params.get('page_size ', 10)
#
#         paginator = Paginator(snippets, page_size)
#         serializer = DiscountSerializer(paginator.page(page_number), many=True, context={'request': request})
#         return Response({
#             'count': snippets.count(),
#             'success': True,
#             'results': serializer.data,
#         }, status=status.HTTP_200_OK)


class DiscountCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############################################################################## FAVORITE


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


