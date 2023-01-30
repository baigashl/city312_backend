from rest_framework import serializers

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items', [])
        cart = Cart.objects.create(**validated_data)

        for item in cart_items_data:
            CartItem.objects.create(cart=cart, **item)

        return cart
