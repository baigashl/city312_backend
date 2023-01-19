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
    activity_type = models.CharField(max_length=255, null=False, blank=False)
    brand_name = models.CharField(max_length=255, null=False, blank=False)
    organization_form = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    inn = models.CharField(max_length=255, null=False, blank=False)
    isVip = models.BooleanField(default=False)
    transaction_quantity = models.IntegerField(default=0, null=True, blank=True)
    logo = models.ImageField(default='default.png', upload_to=upload_logo)
    banner = models.ImageField(default='default.png', upload_to=upload_banner)


    def __str__(self):
        return self.brand_name


class User(MyUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    second_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    discount_card_number = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='user_default.png', upload_to='user_image')

    def __str__(self):
        return f'{self.name}, {self.second_name}'


class PartnerPhoneNumber(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    phone1 = models.CharField(max_length=255, null=True, blank=True)
    phone2 = models.CharField(max_length=255, null=True, blank=True)
    phone3 = models.CharField(max_length=255, null=True, blank=True)
    phone4 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.partner}'


class PartnerSocialMedia(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.partner}'


class WorkingMode(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=255, null=True, blank=True)
    start = models.CharField(max_length=255, null=True, blank=True)
    end = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.partner}'

class Admin(MyUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    second_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}, {self.second_name}'



