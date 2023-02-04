# import stripe
from django.db import models
from django.db.models import Sum, F

from apps.discount.models import Discount
from apps.users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=50, null=True)
    discounts = models.ManyToManyField(Discount, through='CartDiscount')
    total_price = models.IntegerField(default=0)


class CartDiscount(models.Model):
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_cart_total_price(self.cart.id)


def update_cart_total_price(cart_id):
    cart = Cart.objects.get(id=cart_id)
    total_price = CartDiscount.objects.filter(cart=cart).aggregate(
        total_price=Sum(F('discount__price') * F('quantity'))
    )['total_price'] or 0
    cart.total_price = total_price
    cart.save()

# class Payment(models.Model):
#     cart = models.OneToOneField(Cart, null=True, on_delete=models.CASCADE)
#     hashed_card_number = models.CharField(max_length=255, null=True)
#     issued_at = models.DateField(null=True)
#     hashed_cvv = models.IntegerField(null=True)
#     hashed_code = models.IntegerField(null=True)
#
#     def set_card_number(self, card_number):
#         self.hashed_card_number = hash_card_number(card_number)
#
#     def set_cvv(self, cvv):
#         self.set_cvv = hash_cvv(cvv)
#
#     def set_code(self, code):
#         self.set_code = hash_code(code)
