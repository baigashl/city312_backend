from django.db import models

from apps.cart.hash import hash_card_number, hash_cvv, hash_code
from apps.users.models import User
from apps.discount.models import Discount


class Cart(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    hashed_card_number = models.IntegerField(null=True)
    issued_at = models.DateField(null=True)
    hashed_cvv = models.IntegerField(null=True)
    hashed_code = models.IntegerField(null=True)

    def set_card_number(self, card_number):
        self.hashed_card_number = hash_card_number(card_number)

    def set_cvv(self, cvv):
        self.set_cvv = hash_cvv(cvv)

    def set_code(self, code):
        self.set_code = hash_code(code)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, null=True, blank=True, on_delete=models.CASCADE)
    discount = models.ManyToManyField(Discount)
