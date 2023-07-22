from django.test import TestCase
from django_ogp import enums


class Test(TestCase):

    def test_print(self):
        enums._print_mimetypes_enum()
        self.assertTrue(True)
