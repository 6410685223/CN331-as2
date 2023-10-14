from django.db import models
from course.models import Course
# Create your models here.

class student_info(models.Model):

    student_username = models.CharField(max_length=30,primary_key=True)
    student_password = models.CharField(max_length=30)

    student_surname = models.CharField(max_length=30)
    student_lasname = models.CharField(max_length=30)

    def __str__(self) :
        return f"{self.student_surname} {self.student_lasname}: {self.student_username} {self.student_password}"