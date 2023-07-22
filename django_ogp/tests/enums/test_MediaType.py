from django.test import TestCase
from django_ogp import enums


class Test(TestCase):

    def test_value(self):
        self.assertEqual(len(enums.MediaType), 3)
