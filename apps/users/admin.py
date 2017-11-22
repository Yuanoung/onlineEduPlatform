from django.contrib import admin

from .models import UserProfile, EmailVerifyRecord, Banner

admin.site.register(UserProfile)
admin.site.register(EmailVerifyRecord)
admin.site.register(Banner)
