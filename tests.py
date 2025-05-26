from django.test import TestCase
from django.urls import reverse
from .models import Workforce

class WorkforceTests(TestCase):
    def setUp(self):
        Workforce.objects.create(
            name="John Doe", position="Manager", email="john@example.com", hired_date="2023-01-01"
        )

    def test_workforce_list_page_loads(self):
        response = self.client.get(reverse('workforce_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")