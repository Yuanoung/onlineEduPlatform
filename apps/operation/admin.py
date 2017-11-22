from django.contrib import admin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

admin.site.register(UserAsk)
admin.site.register(CourseComments)
admin.site.register(UserFavorite)
admin.site.register(UserMessage)
admin.site.register(UserCourse)
