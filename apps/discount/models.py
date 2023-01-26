from django.db import models
from apps.activity_type.models import Category
from apps.users.models import Partner, User


class DiscountType(models.Model):
    name = models.CharField(max_length=255)


def upload_image(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Discount(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    discount_type = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    price_before = models.IntegerField(default=0, null=False, blank=False)
    price = models.IntegerField(default=0, null=False, blank=False)
    image = models.ImageField(default='default.png', null=True, blank=True, upload_to=upload_image)
    description = models.CharField(max_length=500, null=False, blank=False)
    promotion_condition = models.CharField(max_length=500, null=True, blank=True)
    percentage = models.IntegerField(default=0, null=False, blank=False)
    cashback = models.IntegerField(default=0, null=False, blank=False)
    referral_link = models.CharField(max_length=255, null=False, blank=False)
    start_of_action = models.CharField(max_length=255, null=False, blank=False)
    end_of_action = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
