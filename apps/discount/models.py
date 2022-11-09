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
    discount_type_id = models.ForeignKey(DiscountType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    contacts = models.CharField(max_length=500, null=False, blank=False)
    social_link = models.TextField(null=False, blank=False)
    operating_mode = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(default='default.png', null=True, blank=True, upload_to=upload_image)


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'