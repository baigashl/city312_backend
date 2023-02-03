from rest_framework import serializers
from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for user model registration"""

    class Meta:
        model = User
        exclude = [
            'groups',
            'user_permissions',
            'is_superuser',
        ]
        read_only_fields = [
            'is_active',
            'is_staff',
            'last_login',
        ]


class ClientProfileSerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer()

    class Meta:
        model = ClientProfile
        fields = '__all__'

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        password_data = list(user_data.values())[0]
        user = User.objects.create(**user_data)
        user.set_password(password_data)
        user.save()
        client = ClientProfile.objects.create(user=user, **validated_data)
        client.save()
        return client


class PartnerProfileSerializer(serializers.ModelSerializer):

    user = RegisterUserSerializer()

    class Meta:
        model = PartnerProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password_data = list(user_data.values())[0]
        user = User.objects.create(**user_data)
        user.set_password(password_data)
        user.save()
        client = PartnerProfile.objects.create(user=user, **validated_data)
        client.save()
        return client


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]
