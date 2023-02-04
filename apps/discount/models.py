from django.db import models

from apps.activity_type.models import Category
from apps.users.models import (
    PartnerProfile,
    ClientProfile,
)


class DiscountType(models.Model):
    name = models.CharField(max_length=255)


def upload_image(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Discount(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    partner_id = models.ForeignKey(PartnerProfile, on_delete=models.CASCADE)
    discount_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price_before = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    promotion_condition = models.CharField(max_length=500)
    percentage = models.IntegerField(default=0)
    cashback = models.IntegerField(default=0)
    referral_link = models.CharField(max_length=255)
    start_of_action = models.CharField(max_length=255)
    end_of_action = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class DiscountImage(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(default='default.png', upload_to=upload_image)


class Favorite(models.Model):
    user = models.OneToOneField(ClientProfile, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount)

    def __str__(self):
        return f'{self.user}'
