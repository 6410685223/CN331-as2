from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from course.models import class_of_students,Course
from Students.models import student_info
# Create your tests here.
class HomeViewTest(TestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse('home'))

    def test_Found(self):
        self.assertEqual(self.response.status_code,302)
    
    def test_reverse_login(self):
        self.assertRedirects(self.response, reverse('login'))

class LoginViewTest(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="6410685223",password="kiw123456789")
        self.login_url = reverse('login')
        
    def test_status_code_after_post(self):
        response = self.client.post(self.login_url,{'username':'6410685223','password':'kiw123456789'},follow=True)
        self.assertEqual(response.status_code,200)
        
    def test_login_redirect(self):
        response = self.client.post(self.login_url,{'username':'6410685223','password':'kiw123456789'})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response, reverse('course_list'))

    
    def test_login_invalid(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Expecting a re-render of the login page
        self.assertContains(response, 'Invalid login credentials')
        
