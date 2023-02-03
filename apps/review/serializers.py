# from .models import Comment, Rating
# from rest_framework import serializers
# from rest_framework.reverse import reverse
#
#
# class CommentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#     def get_url(self, obj):
#         request = self.context.get('request')
#         return reverse("detail", kwargs={'id': obj.id}, request=request)
#
#
# class RatingSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Rating
#         fields = '__all__'
#
#     def get_url(self, obj):
#         request = self.context.get('request')
#         return reverse("detail", kwargs={'id': obj.id}, request=request)