from .models import Discount, DiscountType
from rest_framework import serializers
from rest_framework.reverse import reverse


class CourseSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Discount
        fields = ['id', 'mentor', 'name', 'description', 'address', 'start_date', 'active', 'type']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)

