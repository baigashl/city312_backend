from django.contrib import admin
from .models import ActivityType, Category, SubCategory

admin.site.register(ActivityType)
admin.site.register(Category)
admin.site.register(SubCategory)
