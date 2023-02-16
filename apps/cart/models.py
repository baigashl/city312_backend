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
    is_ordered = models.BooleanField(default=False)


class CartDiscount(models.Model):
    cart_id = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_cart_total_price(self.cart_id.id)


def update_cart_total_price(cart_id):
    cart = Cart.objects.get(id=cart_id)
    total_price = CartDiscount.objects.filter(cart_id=cart).aggregate(
        total_price=Sum(F('discount_id__price') * F('quantity'))
    )['total_price'] or 0
    cart.total_price = total_price
    cart.save()
