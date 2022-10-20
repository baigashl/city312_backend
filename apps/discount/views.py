from django.shortcuts import render
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .models import Discount, DiscountType


class DiscountListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = []
    parser_classes = [JSONParser]


