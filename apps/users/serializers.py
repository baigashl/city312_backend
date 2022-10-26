from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Partner
from rest_framework.reverse import reverse
from apps.cart.models import Cart


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
                  'contract_offer',
                  'password',
                  'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'].lower(),
            name=validated_data['name'],
            second_name=validated_data['second_name'],
            date_of_birth=validated_data['date_of_birth'],
            phone_number=validated_data['phone_number'],
            discount_card_number=validated_data['discount_card_number'],
            contract_offer=validated_data['contract_offer'],
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
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

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
            'discount_card_number',
            'contract_offer',
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
        fields = ['email',
                  'activity_type',
                  'brand_name',
                  'organization_form',
                  'phone_number',
                  'description',
                  'inn',
                  'transaction_quantity',
                  # 'isPartner',
                  # 'isVip',
                  'password',
                  'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs

    def create(self, validated_data):
        user = Partner.objects.create(
            email=validated_data['email'],
            activity_type=validated_data['activity_type'],
            brand_name=validated_data['brand_name'],
            organization_form=validated_data['organization_form'],
            phone_number=validated_data['phone_number'],
            description=validated_data['description'],
            inn=validated_data['inn'],
            transaction_quantity=validated_data['transaction_quantity'],
            isPartner=True,
            is_admin=False,
            # isVip=validated_data['isVip'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class PartnerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = [
            'activity_type',
            'brand_name',
            'organization_form',
            'phone_number',
            'description',
            'inn',
            'isVip',
            'transaction_quantity'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)








