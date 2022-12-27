from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.activity_type.models import ActivityType
from apps.users.managers import CustomUserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None
    # Email should be used instead of username
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    isPartner = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


def upload_logo(instance, filename):
    return f'logo/{filename}'.format(filename=filename)

def upload_banner(instance, filename):
    return f'logo/{filename}'.format(filename=filename)


class Partner(MyUser):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.SET_NULL, null=True, blank=True)
    brand_name = models.CharField(max_length=255, null=False, blank=False)
    organization_form = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    inn = models.CharField(max_length=255, null=False, blank=False)
    isVip = models.BooleanField(default=False)
    transaction_quantity = models.IntegerField(default=0, null=True, blank=True)
    logo = models.ImageField(default='default.png', upload_to=upload_logo)
    banner = models.ImageField(default='default.png', upload_to=upload_banner)

    def __str__(self):
        return self.brand_name


class User(MyUser):
    following = models.ManyToManyField(Partner, related_name='following', null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    second_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    discount_card_number = models.CharField(max_length=1000, null=True, blank=True)
    contract_offer = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}, {self.second_name}'


class Admin(MyUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    second_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}, {self.second_name}'



