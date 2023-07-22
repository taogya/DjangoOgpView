
from django.test import TestCase
from django_ogp.enums import MimeType
from django_ogp.models import OgpMimeTypeMaster


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

    def test_after_migrate(self):
        self.assertEqual(OgpMimeTypeMaster.objects.count(), len(MimeType))

    def test_duplicate(self):
        OgpMimeTypeMaster.create_master()
        self.assertEqual(OgpMimeTypeMaster.objects.count(), len(MimeType))
