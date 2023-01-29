from .models import Discount, DiscountType, Favorite
from rest_framework import serializers
from rest_framework.reverse import reverse


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class MultipleImageSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField()
    )


class DiscountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscountType
        fields = ['id', 'name']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)



