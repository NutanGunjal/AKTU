from django.contrib import admin
from .Models.Courses import Courses
from .Models.Syllabus import Syllabus
from .Models.Student import Student

admin.site.register(Courses)
admin.site.register(Syllabus)
admin.site.register(Student)