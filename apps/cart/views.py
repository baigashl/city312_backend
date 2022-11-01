from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cart.models import Cart
from .serializers import CartSerializer
from apps.discount.serializers import DiscountSerializer
from apps.discount.models import Discount


class GetUserCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        snippet = Cart.objects.get(user_id=user_id)
        discounts = snippet.discount.all()
        print('asdasdasd', discounts)
        serializer = CartSerializer(snippet)
        serializer2 = DiscountSerializer(discounts, many=True)
        data = serializer.data
        data['discount'] = serializer2.data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        snippet = Cart.objects.get(user_id=user_id)
        serializer = CartSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        activity_type = Cart.objects.all()
        serializers = CartSerializer(activity_type, many=True)
        return Response(serializers.data)


class CartCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = CartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, user_id):
        try:
            return Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        serializer = CartSerializer(snippet)
        data = serializer.data
        return Response(data)

    def put(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        serializer = CartSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

