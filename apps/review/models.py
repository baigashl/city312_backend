from django.db import models
from apps.users.models import User, Partner


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)



