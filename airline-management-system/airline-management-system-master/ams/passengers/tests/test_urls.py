from django.urls import reverse,resolve
from django.test import SimpleTestCase
from django.test import TestCase, Client
from passengers.views import *

class TestUrls(SimpleTestCase):

    def test_homepage(self):
        url = reverse("passengers:passenger")
        self.assertEquals(resolve(url).func,passenger_homepage)

    def test_book_ticket(self):
        url = reverse("passengers:book")
        self.assertEquals(resolve(url).func, book_ticket)

    def test_search_ticket(self):
        url = reverse('passengers:search')
        self.assertEquals(resolve(url).func, search_flights)

    def test_flight_detail(self):
        url = reverse('passengers:flight',args=['flight-slug'])
        self.assertEquals(resolve(url).func, flight_detail)

    def test_ticket_detail(self):
        url = reverse('passengers:ticket',args=['ticket-slug'])
        self.assertEquals(resolve(url).func, ticket_detail)

    def test_modify_ticket(self):
        url = reverse('passengers:modify_ticket',args=['ticket-slug'])
        self.assertEquals(resolve(url).func, modify_ticket)

    def test_del_ticket(self):
        url = reverse('passengers:del_ticket',args=['ticket-slug'])
        self.assertEquals(resolve(url).func, del_ticket)

    def test_details_of_flight(self):
        url = reverse('passengers:detail',args=['flight-slug'])
        self.assertEquals(resolve(url).func, details_of_flight)

    def test_choose_seat(self):
        url = reverse('passengers:choose_seat',args=['flight-slug'])
        self.assertEquals(resolve(url).func, choose_seat)

    def test_add_details(self):
        url = reverse('passengers:details')
        self.assertEquals(resolve(url).func, add_details)

    def test_add_balane(self):
        url = reverse('passengers:balance')
        self.assertEquals(resolve(url).func, add_balance)

    def test_see_tickets(self):
        url = reverse('passengers:trips')
        self.assertEquals(resolve(url).func, see_tickets)
