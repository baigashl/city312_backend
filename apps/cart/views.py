from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.cart.models import Cart, CartDiscount
from apps.cart.serializers import CartSerializer, CartDiscountSerializer


class CartDiscountViewSet(viewsets.ModelViewSet):
    queryset = CartDiscount.objects.all()
    serializer_class = CartDiscountSerializer

    def get_queryset(self):
        return self.queryset.filter(cart_id__user=self.request.user)

    def create(self, request, *args, **kwargs):
        cart_id = request.data.get('cart_id')
        cart = Cart.objects.get(id=cart_id)

        if cart.is_ordered:
            return Response({'Корзина уже заказана!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
