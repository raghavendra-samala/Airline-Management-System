from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_choose_view(self):
        response = self.client.get(reverse('user_accounts:choose'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_accounts/choose_type.html')

    def test_logout_view(self):
        response = self.client.post(reverse('user_accounts:logout'))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_logout_confirm(self):
        response1 = self.client.get(reverse('user_accounts:logout_confirm'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1,'user_accounts/logout_confirm.html')

    def test_login_view(self):
        response1 = self.client.get(reverse('user_accounts:login'))
        self.assertEquals(response1.status_code,200)
        self.assertTemplateUsed(response1, 'user_accounts/login.html')

    def test_manager_signup(self):
        response = self.client.get(reverse('user_accounts:manager_signup'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user_accounts/manager_signup.html')
        response1 = self.client.post(reverse('user_accounts:manager_signup'))
        self.assertEquals(response1.status_code, 200)

    def test_passenger_signup(self):
        response = self.client.get(reverse('user_accounts:passenger_signup'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user_accounts/passenger_signup.html')
        response1 = self.client.post(reverse('user_accounts:passenger_signup'))
        self.assertEquals(response1.status_code, 200)


