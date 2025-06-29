from django.urls import reverse, resolve
from django.test import SimpleTestCase
from user_accounts.views import PassengerSignup,ManagerSignup,choose_view,login_view,logout_view


class TestUrls(SimpleTestCase):

    def test_homepage(self):
        url = reverse("user_accounts:choose")
        self.assertEquals(resolve(url).func, choose_view)

    def test_PassengerSignUp(self):
        url = reverse("user_accounts:passenger_signup")
        self.assertEquals(resolve(url).func.view_class, PassengerSignup)

    def test_MangerSignUp(self):
        url = reverse('user_accounts:manager_signup')
        self.assertEquals(resolve(url).func.view_class, ManagerSignup)

    def test_login_view(self):
        url = reverse('user_accounts:login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_view(self):
        url = reverse('user_accounts:logout')
        self.assertEquals(resolve(url).func, logout_view)
