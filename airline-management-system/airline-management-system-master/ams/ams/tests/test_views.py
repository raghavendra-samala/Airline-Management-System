from django.test import TestCase, Client
from django.urls import reverse

class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home = reverse('homepage')
        self.help = reverse('help')

    def test_main(self):
        response = self.client.get(self.home)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'homepage.html')

    def test_help(self):
        response = self.client.get(self.help)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'help_main.html')