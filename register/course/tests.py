from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course,class_of_students
from Students.models import student_info
from django.urls import reverse
from .admin import CourseAdmin
# Create your tests here.
class ClassListTestCase(TestCase):
    def setUp(self) -> None:
        # set user
        self.user = User.objects.create_user(username='6410685249',password="first123456789")
        self.client.login(username='6410685249', password='first123456789')
        self.user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',
                                                     student_surname="Siriphatson",student_lasname="sringamphong")       
        # set class
        self.cn202 = Course(course_id="CN202",course_name="Algorithm 2",course_term="1",course_year="2023",
                            avilable_seat=10,course_is_open=True)
        self.cn203 = Course(course_id="CN203",course_name="Algorithm 3",course_term="1",course_year="2023",
                            avilable_seat=10,course_is_open=True)
        self.cn202.save()
        self.cn203.save()

        self.temp = class_of_students.objects.create(student_id="6410685249",student_name="Siriphatson",student_lastname="sringamphong")
        self.temp.course.add("CN202")  
        # set up response
        self.response = self.client.get(reverse('course_list'))
        
    def test_add_couse(self):
        self.assertEqual(self.temp.course.first(), self.cn202)
        
    def test_course_list_response(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_render_template(self):
        self.assertTemplateUsed(self.response, 'course/course_list.html')
    
    def test_response_message(self):
        
        self.assertQuerysetEqual(set(self.response.context['courses']), set(Course.objects.all()))
        self.assertQuerysetEqual(''.join(self.response.context['subject']), Course.objects.get(course_id='CN202').course_id)

class custom_logout(TestCase):
    
    def test_redirect_without_post(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('course_list'))

    def test_redirect_logout_post(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        

class RegisterViewTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        self.user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',
                                                     student_surname="Siriphatson",student_lasname="sringamphong")       

        self.cn202 = Course(course_id="CN202",course_name="Algorithm 2",course_term="1",course_year="2023",
                            avilable_seat=10,course_is_open=True)
        self.cn203 = Course(course_id="CN203",course_name="Algorithm 3",course_term="1",course_year="2023",
                            avilable_seat=10,course_is_open=True)
        self.cn202.save()
        self.cn203.save()
        self.temp = class_of_students.objects.create(student_id="6410685249",student_name="Siriphatson",student_lastname="sringamphong")
        self.temp.course.add("CN202")  
    def test_redirect_mycourse_status(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('mycourse'))

    def test_redirect_course_list_status(self):
        response = self.client.post(reverse('register'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('course_list'))

class Add_to_dbViewTest(TestCase):
        
    def setUp(self):
        self.cn202 = Course(course_id="CN202",course_name="Algorithm 2",course_term="1",
                            course_year="2023",avilable_seat=10,course_is_open=True)
        self.cn203 = Course(course_id="CN203",course_name="Algorithm 3",course_term="1",
                            course_year="2023",avilable_seat=10,course_is_open=True)
        self.cn202.save()
        self.cn203.save()
        user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',
                                                student_surname="Siriphatson",student_lasname="sringamphong")       
        self.temp = class_of_students.objects.create(student_id="6410685249", 
                                                student_name="Siriphatson", student_lastname="sringamphong")
        self.temp.course.add("CN202")

    def test_redirect_course_list(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add'))
        self.assertRedirects(response,reverse('course_list'))
        self.assertEqual(response.status_code,302)
        
    def test_student_info_not_exists(self):
        user = User.objects.create_user(username='6418522350', password='xxx123456789')
        self.client.login(username='6418522350', password='xxx123456789')
        response = self.client.post(reverse('add'))  
        self.assertContains(response, "Student information not found for this user.")
        self.assertEqual(response.status_code,200)
        self.assertEqual(Course.objects.get(course_id='CN202').avilable_seat, 10)

    def test_student_reverse_course_list(self):
        user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        response = self.client.post(reverse('add'),{'course_id':'CN202'})
        
        self.assertRedirects(response,reverse('course_list'))
        self.assertEqual(response.status_code,302)
        self.assertEqual(Course.objects.get(course_id='CN202').avilable_seat,9)

class GetMyCourseTest(TestCase):
    def test_HttpResponseRedirect(self):
        reponse = self.client.get(reverse('get_in_my_course'))
        self.assertRedirects(reponse,reverse('course_list'))
        self.assertEqual(reponse.status_code,302)

    def test_redirect_my_course(self):
        self.user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        self.user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789'
                                                     ,student_surname="Siriphatson",student_lasname="sringamphong")       

        reponse = self.client.post(reverse('get_in_my_course'))
        self.assertRedirects(reponse,reverse('mycourse'))
        self.assertEqual(reponse.status_code,302)

class DeleteCourseTest(TestCase):
    def setUp(self):
        self.cn202 = Course(course_id="CN202",course_name="Algorithm 2",course_term="1",course_year="2023",
                            avilable_seat=10,course_is_open=True)
        self.cn203 = Course(course_id="CN203",course_name="Algorithm 3",course_term="1",course_year="2023",
                            avilable_seat=0,course_is_open=True)
        self.cn202.save()
        self.cn203.save()
        self.temp = class_of_students.objects.create(student_id="6410685249", student_name="Siriphatson", student_lastname="sringamphong")
        self.temp.course.add("CN202")
        self.temp2 = class_of_students.objects.create(student_id="6410685249", student_name="Siriphatson", student_lastname="sringamphong")
        self.temp2.course.add("CN203")

    def test_redirect_mycourse(self):
        user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',
                                                student_surname="Siriphatson",student_lasname="sringamphong")       
        reponse = self.client.get(reverse('delete_subject'))
        self.assertRedirects(reponse,reverse('mycourse'))
        self.assertEqual(reponse.status_code,302)
    def test_post_redirect_mycourse(self):
        user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',
                                                student_surname="Siriphatson",student_lasname="sringamphong")       
        reponse = self.client.post(reverse('delete_subject'),{'course_id':'CN202'})
        self.assertRedirects(reponse,reverse('mycourse'))
        self.assertEqual(reponse.status_code,302)
    
    def test_course_not_open(self):
        cn201 = Course(course_id="CN201",course_name="java",course_term="1",course_year="2023",avilable_seat=10,course_is_open=False)
        self.assertEqual(cn201.course_is_open,False)

    def test_string_course(self):
        cn201 = Course(course_id="CN201",course_name="java",course_term="1",course_year="2023",avilable_seat=10,course_is_open=False)
        self.assertEqual(str(cn201),'CN201 java 1/2023  False')
    
    def test_class_of_student(self):
        self.assertEqual(str(self.temp),'6410685249 Siriphatson sringamphong')
    
    def test_avliable_set(self):
        user = User.objects.create_user(username='6410685249', password='first123456789')
        self.client.login(username='6410685249', password='first123456789')
        user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',student_surname="Siriphatson",student_lasname="sringamphong")       

        self.assertEqual(self.cn203.avilable_seat,0)
    
    def test_admin(self):
        course_admin = CourseAdmin(Course, None)
        students = course_admin.get_students(self.cn202)
        self.assertListEqual(students,['Siriphatson'])
        
    def test_student(self):
        user_info = student_info.objects.create(student_username='6410685249',student_password='first123456789',student_surname="Siriphatson",student_lasname="sringamphong")       
        self.assertEqual(str(user_info),'Siriphatson sringamphong: 6410685249 first123456789')
        