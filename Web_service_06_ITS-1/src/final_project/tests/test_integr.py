from django.test import TestCase
from django.urls import reverse

class AllTests(TestCase):
    def test_form_rendering(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
