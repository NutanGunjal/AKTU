from django.db import models

class Courses(models.Model):
    courseid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False,blank=False)

    def __str__(self):
        return self.name