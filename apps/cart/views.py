from rest_framework import viewsets

from apps.cart.models import Cart
from apps.cart.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
