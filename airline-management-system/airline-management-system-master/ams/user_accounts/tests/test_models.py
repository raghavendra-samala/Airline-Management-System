from django.test import TestCase
from user_accounts.models import User, Passenger,Manager


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='john',
                                              email='jlennon@beatles.com',
                                              password='glass onion',
                                              is_Passenger=True,
                                              balance=10000)
        self.user2 = User.objects.create_user(username='jill',
                                              email='jill@beatles.com',
                                              password='glass onion',
                                              is_Manager=True,
                                              )
        self.passenger1 = Passenger.objects.create(
                               user = self.user1,
                               location = "Hyderabad",
                               phone_number = '9999999999'
                            )
        self.manager1 = Manager.objects.create(
                            user = self.user2,
                            id = '001'
                            )

    def test_passenger(self):
        self.assertEquals(str(self.passenger1),'john')

    def test_manager(self):
        self.assertEquals(str(self.manager1),'jill')