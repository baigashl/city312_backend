from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Discount, DiscountType, Favorite, DiscountImage
from django.core.files.base import ContentFile
import base64
import six
import uuid
from apps.users.serializers import PartnerProfileSerializer


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class DiscountImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = DiscountImage
        fields = ('id', 'discount', 'image',)


class DiscountListSerializer(serializers.ModelSerializer):
    images = DiscountImageSerializer(many=True, required=False)
    partner_id = PartnerProfileSerializer(required=False)

    class Meta:
        model = Discount
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    images = DiscountImageSerializer(many=True, required=False)
    uploaded_images = serializers.ListField(
        child=Base64ImageField(),
        write_only=True,
        required=False
    )
    update_images = serializers.DictField(
        child=Base64ImageField(),
        write_only=True,
        required=False
    )
    delete_images = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
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

    def update(self, instance, validated_data):
        discount_id = instance.id
        discount = Discount.objects.get(id=discount_id)
        discount.discount_type = validated_data['discount_type']
        discount.name = validated_data['name']
        discount.price_before = validated_data['price_before']
        discount.price = validated_data['price']
        discount.description = validated_data['description']
        discount.promotion_condition = validated_data['promotion_condition']
        discount.percentage = validated_data['percentage']
        discount.cashback = validated_data['cashback']
        discount.referral_link = validated_data['referral_link']
        discount.start_of_action = validated_data['start_of_action']
        discount.end_of_action = validated_data['end_of_action']
        discount.save()

        if 'uploaded_images' in validated_data.keys():
            for image in validated_data['uploaded_images']:
                DiscountImage.objects.create(discount_id=discount_id, image=image)

        if 'update_images' in validated_data.keys():
            print(validated_data['update_images'])
            for image_id, img in validated_data['update_images'].items():
                obj = DiscountImage.objects.get(id=image_id)
                obj.image = img
                obj.save()

        if 'delete_images' in validated_data.keys():
            for id in validated_data['delete_images']:
                obj = DiscountImage.objects.get(id=id)
                obj.delete()

        return discount


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
