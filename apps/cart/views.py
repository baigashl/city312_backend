from rest_framework import viewsets

from apps.cart.models import Cart, CartDiscount
from apps.cart.serializers import CartSerializer, CartDiscountSerializer


class CartDiscountViewSet(viewsets.ModelViewSet):
    queryset = CartDiscount.objects.all()
    serializer_class = CartDiscountSerializer

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
