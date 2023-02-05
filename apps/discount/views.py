from django.http import Http404
from rest_framework import pagination
from rest_framework import permissions, status, filters, viewsets
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Discount, DiscountImage
from .serializers import DiscountSerializer, DiscountUpdateSerializer, DiscountImageSerializer
from ..users.permissions import AnonPermissionOnly


# class CustomPagination(pagination.PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 50
#     page_query_param = 'p'

###################################################################
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.AllowAny]
    parser_class = [MultiPartParser, FormParser, JSONParser]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'price', 'cashback']
    search_fields = ['name', 'partner_id__brand_name']
##################################################################################





# ############################################################################## FAVORITE


# class GetUserFavoriteAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request, user_id):
#         snippet = Favorite.objects.get(user_id=user_id)
#         discounts = snippet.discount.all()
#         print('asdasdasd', discounts)
#         serializer = FavoriteSerializer(snippet)
#         serializer2 = DiscountSerializer(discounts, many=True)
#         data = serializer.data
#         data['discount'] = serializer2.data
#         return Response(data, status=status.HTTP_200_OK)
#
#     def patch(self, request, user_id):
#         snippet = Favorite.objects.get(user_id=user_id)
#         serializer = FavoriteSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class FavoriteListAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         activity_type = Favorite.objects.all()
#         serializers = FavoriteSerializer(activity_type, many=True)
#         return Response(serializers.data)
#
#
# class FavoriteCreateAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         serializers = FavoriteSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class FavoriteDetailAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     parser_classes = [JSONParser]
#
#     def get_object(self, user_id):
#         try:
#             return Favorite.objects.get(user_id=user_id)
#         except Favorite.DoesNotExist:
#             raise Http404
#
#     def get(self, request, user_id, format=None):
#         snippet = self.get_object(user_id)
#         serializer = FavoriteSerializer(snippet)
#         data = serializer.data
#         return Response(data)
#
#     def put(self, request, user_id, format=None):
#         snippet = self.get_object(user_id)
#         serializer = FavoriteSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, user_id, format=None):
#         snippet = self.get_object(user_id)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class AddToFavoriteAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def patch(self, request):
#         serializers = FavoriteSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)