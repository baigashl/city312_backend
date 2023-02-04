from django.urls import path, include
from rest_framework import routers

from .views import CartViewSet, CartDiscountViewSet

router = routers.DefaultRouter()
router.register(r'cart_item', CartDiscountViewSet)
router.register(r'carts', CartViewSet)
# router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
