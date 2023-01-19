from django.contrib import admin
from .models import MyUser, User, PartnerPhoneNumber, PartnerSocialMedia
from .models import Partner

admin.site.register(Partner)
admin.site.register(MyUser)
admin.site.register(User)
admin.site.register(PartnerPhoneNumber)
admin.site.register(PartnerSocialMedia)
