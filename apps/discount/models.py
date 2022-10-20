from django.db import models
from apps.activity_type.models import Category
from apps.users.models import Partner


class DiscountType(models.Model):
    name = models.CharField(max_length=255)


class Discount(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    discount_type_id = models.ForeignKey(DiscountType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    contacts = models.CharField(max_length=500, null=False, blank=False)
    social_link = models.TextField(null=False, blank=False)
    operating_mode = models.CharField(max_length=255, null=False, blank=False)


