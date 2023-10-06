from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id','course_name','get_students']

    @admin.display(description='students')
    def get_students(self, obj):

        return [set(class_of_students.student_name for class_of_students in obj.class_of_students_set.all())]


# admin.site.register(Course)
admin.site.register(class_of_students)