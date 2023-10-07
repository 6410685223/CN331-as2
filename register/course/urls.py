from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('add/',views.add_to_DB,name='add'),
    path('my_course/',views.my_course,name='mycourse'),
    path('delete/',views.delete_subject,name='delete_subject'),
    path('get_in_my_course/',views.get_in_my_course,name='get_in_my_course'),
    path('Register/',views.register,name='register'),
    path('logout/',views.custom_logout,name='logout'),
]