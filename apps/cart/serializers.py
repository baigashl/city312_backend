from rest_framework import serializers

from .models import Cart, CartDiscount


class CartDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDiscount
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ["total_price"]

# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'
#
#     def create(self, validated_data):
#         payment = Payment.objects.create(**validated_data)
#         cart = self.context['cart']
#         email = self.context['email']
#         payment.charge(cart, email)
#         return payment
