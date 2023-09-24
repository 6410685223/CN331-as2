from django.db import models
from django.core.validators import MinValueValidator
import datetime
# Create your models here.


class Course(models.Model):
    
    YEAR_CHOICES = []
    for r in range(datetime.datetime.now().year, (datetime.datetime.now().year+10)):
        YEAR_CHOICES.append((r,r))

    term_choice = (("1","1"),("2","2"),("Summer","Summer"))
    
    course_id = models.CharField(max_length=5,primary_key=True)
    course_name = models.CharField(max_length=100)
    course_term = models.CharField(max_length=6,choices=term_choice,default="1")
    course_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    student_amount = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    course_is_open = models.BooleanField(default=False)
    

    def __str__(self) :
        return f"{self.course_id} {self.course_name} {self.course_term}/{self.course_year}"