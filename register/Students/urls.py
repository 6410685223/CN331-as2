
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your student app
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]
