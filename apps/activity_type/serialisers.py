from .models import ActivityType
from rest_framework import serializers
from rest_framework.reverse import reverse


class ActivityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityType
        fields = ['id', 'name']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityType
        fields = ['id', 'activity_type', 'name']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)
