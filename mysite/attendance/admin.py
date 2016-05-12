from django.contrib import admin

# Register your models here.
from attendance.models import Student
from attendance.models import Score
from attendance.models import Subject
from attendance.models import Statistics

admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Subject)
admin.site.register(Statistics)