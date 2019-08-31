from django.contrib import admin
from .models import Profile, Grade, Assignment, Course, GradeAssignments

admin.site.register(Profile)
admin.site.register(Grade)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(GradeAssignments)