from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('add/',views.add_to_DB,name='add')
]