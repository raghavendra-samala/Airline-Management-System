from django.test import TestCase
from passengers.models import Tickets
from user_accounts.models import User, Passenger


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='john',
                                              email='jlennon@beatles.com',
                                              password='glass onion',
                                              is_Passenger=True,
                                              balance=10000)
        self.ticket1 = Tickets.objects.create(
            booking_id='hc2021-04-09',
            from_station='Hyderabad',
            to_station='Chennai',
            seat_type='economy',
            seat_number=5,
            ticket_holder=self.user1,
            fare=2500
        )

    def test_slug_pnr(self):
        self.assertEquals(self.ticket1.slug, 'hc2021-04-09e5')
        self.assertEquals(self.ticket1.pnr, 'hc2021-04-09e5')

    def test_expected_object_name(self):
        self.assertEquals(self.ticket1.slug,str(self.ticket1))

    def test_user_balance(self):
        self.assertEquals(self.ticket1.ticket_holder.balance, 7500)


