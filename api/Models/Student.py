from django.db import models

from .Courses import Courses
from .Syllabus import Syllabus

class Student(models.Model):
    name = models.CharField(max_length=200, null=False,blank=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name