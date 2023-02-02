from django.contrib import admin
from apps.users.models import User, PartnerProfile, ClientProfile

admin.site.register(User)
admin.site.register(PartnerProfile)
admin.site.register(ClientProfile)
