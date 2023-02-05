from rest_framework import serializers
from rest_framework_recaptcha.fields import ReCaptchaField

from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model registration"""

    class Meta:
        model = User
        exclude = [
            'groups',
            'user_permissions',
        ]
        read_only_fields = [
            'is_active',
            'is_staff',
            'last_login',
            'is_superuser',
        ]


class ClientProfileSerializer(serializers.ModelSerializer):
    """Serializer for ClientProfile model"""

    user = UserSerializer()
    captcha = ReCaptchaField()

    class Meta:
        model = ClientProfile
        fields = '__all__'

    def create(self, validated_data):
        """Create nested UserSerializer fields"""

        user_data = validated_data.pop('user')
        password_data = list(user_data.values())[0]
        user = User.objects.create(**user_data)
        user.set_password(password_data)
        user.save()
        client = ClientProfile.objects.create(user=user, **validated_data)
        client.save()
        return client

    def update(self, instance, validated_data):
        """Update nested UserSerializer fields """

        if 'user' in validated_data:
            nested_serializer = self.fields['user']
            nested_instance = instance.user
            nested_data = validated_data.pop('user')
            nested_serializer.update(nested_instance, nested_data)
        return super(ClientProfileSerializer, self).update(instance, validated_data)


class PartnerProfileSerializer(serializers.ModelSerializer):
    """Serializer for PartnerProfile model"""

    user = UserSerializer()
    captcha = ReCaptchaField()

    class Meta:
        model = PartnerProfile
        fields = '__all__'

    def create(self, validated_data):
        """Create nested UserSerializer fields"""

        user_data = validated_data.pop('user')
        password_data = list(user_data.values())[0]
        user = User.objects.create(**user_data)
        user.set_password(password_data)
        user.save()
        client = PartnerProfile.objects.create(user=user, **validated_data)
        client.save()
        return client

    def update(self, instance, validated_data):
        """Update nested UserSerializer fields """

        if 'user' in validated_data:
            nested_serializer = self.fields['user']
            nested_instance = instance.user
            nested_data = validated_data.pop('user')
            nested_serializer.update(nested_instance, nested_data)
        return super(PartnerProfileSerializer, self).update(instance, validated_data)


class LoginUserSerializer(serializers.ModelSerializer):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "captcha"
        ]
