from django.shortcuts import render
from .models import Course,class_of_students
from .forms import CustomUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Students.models import student_info

# Create your views here.
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {
        'courses': courses,
    })

@login_required
def add_to_DB(request):
    if request.method == 'POST':

        try:
            student_info_obj = student_info.objects.get(student_username=request.user)
        except student_info.DoesNotExist:
            return HttpResponse("Student information not found for this user.")

        course_name = request.POST.get('course_name')

        # Create a new Student instance
        student_instance = class_of_students.objects.create(
            student_id=str(student_info_obj.student_username),
            student_surname=str(student_info_obj.student_surname),
            student_lasname=str(student_info_obj.student_lasname),
            course_name=str(course_name),
        )
        print(student_instance)
        student_instance.save()
        # Redirect to the course list page
        return HttpResponseRedirect(reverse('course_list'))

    return HttpResponseRedirect(reverse('course_list'))
