import stripe
from decouple import config
from django.test import TestCase

from apps.cart.models import Cart, Payment

stripe.api_key = config("STRIPE")


class PaymentTestCase(TestCase):
    def setUp(self):
        # Create a cart and a payment
        self.cart = Cart.objects.create()
        self.payment = Payment.objects.create(cart=self.cart)

    def test_charge(self):
        # Use the Stripe testing API to simulate the payment process
        self.payment.hashed_card_number = "tok_visa"  # Use a test card token
        self.payment.issued_at = "2022-02-02"
        self.payment.hashed_cvv = 123
        self.payment.hashed_code = 123
        self.payment.save()

        charge = self.payment.charge(self.cart, "test@example.com")

        # Check if the charge was successful
        self.assertEqual(charge["amount"], int(self.cart.total_price * 100))
        self.assertEqual(charge["currency"], "kgs")
        self.assertEqual(charge["receipt_email"], "test@example.com")
