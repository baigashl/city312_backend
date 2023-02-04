from rest_framework import viewsets, permissions

from apps.cart.models import Cart, CartDiscount
from apps.cart.serializers import CartSerializer, CartDiscountSerializer


class CartDiscountViewSet(viewsets.ModelViewSet):
    queryset = CartDiscount.objects.all()
    serializer_class = CartDiscountSerializer
    permission_classes = [permissions.AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny]

# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
