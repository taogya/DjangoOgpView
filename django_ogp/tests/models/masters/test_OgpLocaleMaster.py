
from django.test import TestCase
from django_ogp.enums import Locale
from django_ogp.models import OgpLocaleMaster


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

    def test_after_migrate(self):
        self.assertEqual(OgpLocaleMaster.objects.count(), len(Locale))

    def test_duplicate(self):
        OgpLocaleMaster.create_master()
        self.assertEqual(OgpLocaleMaster.objects.count(), len(Locale))
