from django.db import models
from .Courses import Courses

class Syllabus(models.Model):
    name = models.CharField(max_length=200, null=False,blank=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name