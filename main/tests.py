from django.test import TestCase
from django.urls import reverse

class MainAppTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
