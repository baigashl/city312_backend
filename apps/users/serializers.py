
from rest_framework import serializers
from rest_framework_recaptcha.fields import ReCaptchaField
import base64
import six
import uuid

from django.core.files.base import ContentFile
from apps.users.models import (
    User,
    ClientProfile,
    PartnerProfile,
)


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile


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
    image = Base64ImageField()
    # captcha = ReCaptchaField()

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
    # captcha = ReCaptchaField()

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

    class Meta:
        model = User
        fields = [
            "email",
            "password"
        ]
