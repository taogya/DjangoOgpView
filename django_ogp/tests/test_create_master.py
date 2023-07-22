
from django.test import TestCase
from django_ogp.enums import Locale, MimeType
from django_ogp.models import OgpLocaleMaster, OgpMimeTypeMaster


class Test(TestCase):

    def test_create_master(self):
        self.assertEqual(OgpLocaleMaster.objects.count(), len(Locale))
        self.assertEqual(OgpMimeTypeMaster.objects.count(), len(MimeType))
