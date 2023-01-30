from django.urls import path, include
from rest_framework import routers

from .views import CartViewSet

router = routers.DefaultRouter()
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
