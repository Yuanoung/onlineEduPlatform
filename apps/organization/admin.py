from django.contrib import admin

from .models import CityDict, CourseOrg, Teacher

admin.site.register(CityDict)
admin.site.register(CourseOrg)
admin.site.register(Teacher)
