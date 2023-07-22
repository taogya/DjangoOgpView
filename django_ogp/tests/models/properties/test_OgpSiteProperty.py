
from django.test import TestCase
from django_ogp.models import OgpSiteProperty


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

    def test_empty(self):
        # フォームからの入力の場合は、空文字を許容しない。
        OgpSiteProperty.objects.create()

        self.assertEqual(OgpSiteProperty.objects.count(), 1)

    def test_create(self):
        OgpSiteProperty.objects\
            .create(name='Test Site')

        self.assertEqual(OgpSiteProperty.objects.count(), 1)

    def test_duplicate(self):
        OgpSiteProperty.objects\
            .create(name='Test Site')
        OgpSiteProperty.objects\
            .create(name='Test Site')

        self.assertEqual(OgpSiteProperty.objects.count(), 2)
