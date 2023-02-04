# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from apps.activity_type.models import ActivityType
# from apps.users.managers import CustomUserManager
#
#
# class MyUser(AbstractBaseUser, PermissionsMixin):
#     username = None
#     # Email should be used instead of username
#     email = models.EmailField('email address', unique=True)
#     password = models.CharField(max_length=255, null=False, blank=False)
#
#     isPartner = models.BooleanField(default=False)
#
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return f'{self.email}'
#
#
# def upload_logo(instance, filename):
#     return f'logo/{filename}'.format(filename=filename)
#
# def upload_banner(instance, filename):
#     return f'banner/{filename}'.format(filename=filename)
#
#
# class Partner(MyUser):
#     activity_type = models.CharField(max_length=255, null=False, blank=False)
#     brand_name = models.CharField(max_length=255, null=False, blank=False)
#     organization_form = models.CharField(max_length=255, null=False, blank=False)
#     description = models.CharField(max_length=1000, null=True, blank=True)
#     inn = models.CharField(max_length=255, null=False, blank=False)
#     isVip = models.BooleanField(default=False)
#     transaction_quantity = models.IntegerField(default=0, null=True, blank=True)
#     logo = models.ImageField(default='default.png', upload_to=upload_logo)
#     banner = models.ImageField(default='default.png', upload_to=upload_banner)
#     phone1 = models.CharField(max_length=255, null=False, blank=False)
#     phone2 = models.CharField(max_length=255, null=True, blank=True)
#     phone3 = models.CharField(max_length=255, null=True, blank=True)
#     phone4 = models.CharField(max_length=255, null=True, blank=True)
#     whatsapp = models.CharField(max_length=255, null=True, blank=True)
#     youtube = models.CharField(max_length=255, null=True, blank=True)
#     telegram = models.CharField(max_length=255, null=True, blank=True)
#     facebook = models.CharField(max_length=255, null=True, blank=True)
#     schedule = models.CharField(max_length=255, null=False, blank=False)
#     start = models.CharField(max_length=255, null=False, blank=False)
#     end = models.CharField(max_length=255, null=False, blank=False)
#
#
#     def __str__(self):
#         return self.brand_name
#
#
# class User(MyUser):
#     name = models.CharField(max_length=255, null=False, blank=False)
#     second_name = models.CharField(max_length=255, null=False, blank=False)
#     date_of_birth = models.CharField(max_length=255, null=False, blank=False)
#     phone_number = models.CharField(max_length=255, null=False, blank=False)
#     discount_card_number = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ImageField(default='user_default.png', upload_to='user_image')
#
#     def __str__(self):
#         return f'{self.name}, {self.second_name}'
#
#
#
# class Admin(MyUser):
#     name = models.CharField(max_length=255, null=False, blank=False)
#     second_name = models.CharField(max_length=255, null=False, blank=False)
#     date_of_birth = models.CharField(max_length=255, null=False, blank=False)
#     phone_number = models.CharField(max_length=255, null=False, blank=False)
#
#     def __str__(self):
#         return f'{self.name}, {self.second_name}'


from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def upload_logo(instance, filename):
    return f'logo/{filename}'.format(filename=filename)


def upload_banner(instance, filename):
    return f'banner/{filename}'.format(filename=filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Methode creates user
        :param email: str
        :param password: str
        :param extra_fields: dict
        :return: User
        """
        if not email:
            raise ValueError("Нужно ввести email")
        if not password:
            raise ValueError("Нужно ввести пароль")

        user = self.model(
            email=email,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Methode creates superuser
        :param email: str
        :param password: str
        :return: superuser
        """
        user = self.model(
            email=email,
            password=password,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.user_type = 3
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    client = 'Клиент'
    partner = 'Партнер'
    admin = 'Администратор'
    user_type_choices = [
        (client, 'Клиент'),
        (partner, 'Партнер'),
        (admin, 'Администратор'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255, choices=user_type_choices, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'


class PartnerProfile(models.Model):
    """Partner profile model"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=255, null=False, blank=False)
    organization_form = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    inn = models.CharField(max_length=255)
    isVip = models.BooleanField(default=False)
    transaction_quantity = models.IntegerField(default=0, null=True, blank=True)
    logo = models.ImageField(default='default.png', upload_to=upload_logo, null=True, blank=True)
    banner = models.ImageField(default='default.png', upload_to=upload_banner, null=True, blank=True)
    phone_number2 = models.CharField(max_length=255, null=True, blank=True)
    phone_number3 = models.CharField(max_length=255, null=True, blank=True)
    phone_number4 = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    schedule = models.CharField(max_length=255, null=False, blank=False)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.brand_name}'


class ClientProfile(models.Model):
    """Client profile model"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    discount_card_number = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='user_default.png', upload_to='user_image', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
