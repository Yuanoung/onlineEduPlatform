from django.contrib import admin

from .models import Course, BannerCourse, Lesson, Video, CourseResource

admin.site.register(Course)
admin.site.register(BannerCourse)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(CourseResource)
