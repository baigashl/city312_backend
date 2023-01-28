from django.db import models
from apps.users.models import User
from apps.discount.models import Discount


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount)
