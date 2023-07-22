
from django.db import transaction
from django.test import TestCase
from django_ogp.enums import OgpType
from django_ogp.models import OgpCustomProperty, OgpSiteProperty


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        OgpSiteProperty.objects\
            .create(name='Test Site')

    def test_empty(self):
        from django.db.utils import IntegrityError

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpCustomProperty.objects.create()
        self.assertEqual(OgpCustomProperty.objects.count(), 0)

        # フォームからの入力の場合は、['type', 'url']の空文字を許容しない。
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpCustomProperty.objects\
                    .create(site=OgpSiteProperty.objects.first(),
                            type=OgpType.book,
                            url='http://example.com/')
        self.assertEqual(OgpCustomProperty.objects.count(), 0)

        OgpCustomProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    type=OgpType.book,
                    url='http://example.com/',
                    property='{"book:author": "Test User", "book:tag": "novel"}')
        self.assertEqual(OgpCustomProperty.objects.count(), 1)

    def test_create(self):
        OgpCustomProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    type=OgpType.book,
                    url='http://example.com/',
                    property='{"book:author": "Test User", "book:tag": "novel"}')

        self.assertEqual(OgpSiteProperty.objects.count(), 1)

    def test_duplicate(self):
        OgpCustomProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    type=OgpType.book,
                    url='http://example.com/',
                    property='{"book:author": "Test User", "book:tag": "novel"}')
        OgpCustomProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    type=OgpType.book,
                    url='http://example.com/',
                    property='{"book:author": "Test User", "book:tag": "novel"}')

        self.assertEqual(OgpSiteProperty.objects.count(), 1)
