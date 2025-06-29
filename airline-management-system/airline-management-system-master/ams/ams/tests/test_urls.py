from django.urls import reverse, resolve
from django.http import HttpRequest
from django.test import SimpleTestCase
from ams.views import homepage,help_main


class TestUrls(SimpleTestCase):

    def test_homepage(self):
        url = reverse("homepage")
        #response = self.get.client(url)
        self.assertEquals(resolve(url).func, homepage)
        #self.assertTemplateUsed(response,'homepage.html')

    def test_help(self):
        url = reverse("help")
        self.assertEquals(resolve(url).func, help_main)
