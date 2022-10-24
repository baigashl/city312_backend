from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Discount, DiscountType
from .serializers import DiscountSerializer, DiscountTypeSerializer

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

