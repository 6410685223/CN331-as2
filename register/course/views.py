from django.shortcuts import render, redirect
from .models import Course,class_of_students
from .forms import CustomUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Students.models import student_info
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

def course_list(request):

    courses = Course.objects.all()
    check = set()    
    for i in class_of_students.objects.values_list('student_id','course'):
        if str(i[0]) == str(request.user):
            check.add(i[1])
    return render(request, 'course/course_list.html', {
        'courses': courses,
        'subject': check,
    })

@login_required
def add_to_DB(request):
    if request.method == 'POST':
        try:
            student_info_obj = student_info.objects.get(student_username=request.user)
        except student_info.DoesNotExist:
            return HttpResponse("Student information not found for this user.")

        course_name = request.POST.get('course_name')
        course = Course.objects.get(course_name=course_name)
        # Create a new Student instance
        student_instance = class_of_students.objects.create(
            student_id=str(student_info_obj.student_username),
            student_name=str(student_info_obj.student_surname),
            student_lastname=str(student_info_obj.student_lasname),
        )
        student_instance.course.add(course.course_id)
        student_instance.save()

        # print(class_of_students.objects.filter(student_id=request.user).last())
        check = set()    
        for i in class_of_students.objects.values_list('student_id','course'):
            # print(i[0] + " " + request.user)
            if str(i[0]) == str(request.user):
                check.add(i[1])
        messages.success(request, list(check))

        # Redirect to the course list page
        return redirect(reverse('add'))

    return HttpResponseRedirect(reverse('course_list'))
