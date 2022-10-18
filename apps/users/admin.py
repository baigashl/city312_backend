from django.contrib import admin
from .models import MyUser, CustomUser
from .models import Partner

admin.site.register(Partner)
admin.site.register(MyUser)
admin.site.register(CustomUser)
