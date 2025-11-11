from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from taxi.models import Manufacturer, Car


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin", password="12345"
        )
        self.client.login(username="admin", password="12345")

        self.manufacturer = Manufacturer.objects.create(name="Toyota")
        self.car = Car.objects.create(model="Corolla", manufacturer=self.manufacturer)

    def test_search_driver(self):
        response = self.client.get(reverse("driver-list"), {"search": "admin"})
        self.assertContains(response, "admin")

    def test_search_car(self):
        response = self.client.get(reverse("car-list"), {"search": "Corolla"})
        self.assertContains(response, "Corolla")

    def test_search_manufacturer(self):
        response = self.client.get(reverse("manufacturer-list"), {"search": "Toyota"})
        self.assertContains(response, "Toyota")
