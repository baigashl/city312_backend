from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from drf_writable_nested import WritableNestedModelSerializer

from .models import Cart, CartDiscount
from ..discount.models import Discount
from ..discount.serializers import DiscountListSerializer


class CartDiscountSerializer(WritableNestedModelSerializer):
    discount_id = PresentablePrimaryKeyRelatedField(
        queryset=Discount.objects.all(),
        presentation_serializer=DiscountListSerializer,
    )

    class Meta:
        model = CartDiscount
        fields = '__all__'


class CartSerializer(WritableNestedModelSerializer):
    # discounts = PresentablePrimaryKeyRelatedField(
    #     queryset=CartDiscount.objects.all(),
    #     presentation_serializer=CartDiscountSerializer,
    #     # read_only=True
    #     # presentation_serializer=CartDiscountSerializer
    # )

    # discounts = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id',
                  'user',
                  'email',
                  'name',
                  'discounts',
                  'total_price',
                  'is_ordered']
        read_only_fields = ['total_price']
