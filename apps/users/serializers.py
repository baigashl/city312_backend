from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Partner, Admin
from rest_framework.reverse import reverse
from apps.cart.models import Cart
from ..discount.models import Favorite


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        token['is_admin'] = user.is_admin
        token['isPartner'] = user.isPartner

        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )


    class Meta:
        model = User
        fields = ['email',
                  'name',
                  'second_name',
                  'date_of_birth',
                  'phone_number',
                  'discount_card_number',
                  'image',
                  'password',
                  'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs

    def create(self, validated_data):
        if 'image' in list(validated_data.keys()):
            image = validated_data['image'],
        else:
            image = None
        user = User.objects.create(
            email=validated_data['email'].lower(),
            name=validated_data['name'],
            second_name=validated_data['second_name'],
            date_of_birth=validated_data['date_of_birth'],
            phone_number=validated_data['phone_number'],
            discount_card_number=validated_data['discount_card_number'],
            image = image,
            isPartner=False,
            is_admin=False,
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        cart = Cart.objects.create(
            user=user
        )
        cart.save()
        favorite = Favorite.objects.create(
            user=user
        )
        favorite.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'second_name',
            'date_of_birth',
            'phone_number',
            'image',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'second_name',
            'date_of_birth',
            'phone_number',
            'image',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class PartnerRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Partner.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = Partner
        fields = [
            'id',
          'email',
          'activity_type',
          'brand_name',
          'organization_form',
          'description',
          'inn',
          'password',
          'password2',
          'logo',
          'banner',
            'phone1',
            'phone2',
            'phone3',
            'phone4',
            'whatsapp',
            'youtube',
            'telegram',
            'facebook',
            'schedule',
            'start',
            'end'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = [
            'id',
            'email',
            'isPartner',
            'is_admin',
            'brand_name',
            'organization_form',
            'description',
            'inn',
            'isVip',
            'transaction_quantity',
            'logo',
            'banner',
            'activity_type',
            'phone1',
            'phone2',
            'phone3',
            'phone4',
            'whatsapp',
            'youtube',
            'telegram',
            'facebook',
            'schedule',
            'start',
            'end'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

