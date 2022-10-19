from django.contrib import admin
from .models import MyUser, User
from .models import Partner

admin.site.register(Partner)
admin.site.register(MyUser)
admin.site.register(User)
