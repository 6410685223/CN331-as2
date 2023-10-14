from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_view(request,*args, **kwargs):
    return HttpResponseRedirect(reverse('login'))

def login_view(request):
    if request.method == 'POST':
        # Perform authentication
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('course_list'))
        return render(request, 'registration/login.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'registration/login.html')  # Display the login page