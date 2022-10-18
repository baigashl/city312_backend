from django.db import models
from apps.users.models import CustomUser
from apps.discount.models import Discount


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount, null=True, blank=True)
