from django.urls import reverse, resolve
from django.test import SimpleTestCase
from managers.views import *

class TestUrls(SimpleTestCase):

    def test_homepage(self):
        url = reverse("managers:manager")
        self.assertEquals(resolve(url).func, manager_homepage)

    def test_check_occupancy(self):
        url = reverse("managers:check")
        self.assertEquals(resolve(url).func, check_occupancy)

    def test_change_schedule(self):
        url = reverse('managers:change')
        self.assertEquals(resolve(url).func, change_schedule)

    def test_get_profits(self):
        url = reverse('managers:profit')
        self.assertEquals(resolve(url).func, get_profits)

    def test_add_flight(self):
        url = reverse('managers:add')
        self.assertEquals(resolve(url).func, add_flight)

    def test_delete_flight(self):
        url = reverse('managers:delete')
        self.assertEquals(resolve(url).func, delete_flight)

    def test_del_flight(self):
        url = reverse('managers:del', args=['flight-slug'])
        self.assertEquals(resolve(url).func, del_flight)

    def test_view_occupancy(self):
        url = reverse('managers:view_occupancy')
        self.assertEquals(resolve(url).func, view_occupancy)

    def test_change_costs(self):
        url = reverse('managers:costs')
        self.assertEquals(resolve(url).func, change_costs)

    def test_modify_costs(self):
        url = reverse('managers:modify')
        self.assertEquals(resolve(url).func, modify_costs)
