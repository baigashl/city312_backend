from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Discount, DiscountType, Favorite, DiscountImage


class DiscountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = ('id', 'discount', 'image',)


class DiscountSerializer(serializers.ModelSerializer):
    images = DiscountImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Discount
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        discount = Discount.objects.create(**validated_data)

        for image in uploaded_images:
            DiscountImage.objects.create(discount=discount, image=image)

        return discount

    # def update(self, instance, validated_data):
    #     images = validated_data.pop("uploaded_images")
    #
    #     for image in images:
    #         if image['id']:
    #             if DiscountImage.objects.filter(image=image).exists():
    #                 obj = DiscountImage.objects.get(id=image['id'])
    #                 obj.image = image['image']





class DiscountUpdateSerializer(serializers.ModelSerializer):
    images = DiscountImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Discount
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     uploaded_images = validated_data.pop("uploaded_images")
    #     discount = Discount.objects.update(**validated_data)
    #
    #     for image in uploaded_images:
    #         DiscountImage.objects.update(discount=discount, image=image)
    #
    #     return discount


# class DiscountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Discount
#         fields = '__all__'

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
