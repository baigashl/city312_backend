from .models import Discount, DiscountType
from rest_framework import serializers
from rest_framework.reverse import reverse


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class DiscountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscountType
        fields = ['id', 'name']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

