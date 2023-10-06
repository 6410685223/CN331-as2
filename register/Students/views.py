# views.py in your student app

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import Course
@login_required
def student_dashboard(request):
    # This view is only accessible to logged-in users
    # You can add logic here to display student-specific dashboard content
    return render(request, 'registor/regist.html')

