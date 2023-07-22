
from django.db import transaction
from django.test import TestCase
from django_ogp.enums import MediaType
from django_ogp.models import OgpMediaProperty


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

    def test_empty(self):
        from django.db.utils import IntegrityError

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpMediaProperty.objects.create()
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpMediaProperty.objects.create(media_type=MediaType.image)
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpMediaProperty.objects.create(media_type=MediaType.image,
                                                url='http://example.com/static/image/test.png')
        self.assertEqual(OgpMediaProperty.objects.count(), 0)

        # フォームからの入力の場合は、['alt']の空文字を許容しない。
        OgpMediaProperty.objects\
            .create(media_type=MediaType.image,
                    url='http://example.com/static/image/test.png',
                    type_id='image/png',
                    alt='Test Image')
        self.assertEqual(OgpMediaProperty.objects.count(), 1)

    def test_create(self):
        OgpMediaProperty.objects\
            .create(media_type=MediaType.image,
                    url='http://example.com/static/image/test.png',
                    secure_url='https://example.com/static/image/test.png',
                    type_id='image/png',
                    alt='Test Image',
                    width=1200,
                    height=630)

        self.assertEqual(OgpMediaProperty.objects.count(), 1)

    def test_duplicate(self):
        OgpMediaProperty.objects\
            .create(media_type=MediaType.image,
                    url='http://example.com/static/image/test.png',
                    secure_url='https://example.com/static/image/test.png',
                    type_id='image/png',
                    alt='Test Image',
                    width=1200,
                    height=630)
        OgpMediaProperty.objects\
            .create(media_type=MediaType.image,
                    url='http://example.com/static/image/test.png',
                    secure_url='https://example.com/static/image/test.png',
                    type_id='image/png',
                    alt='Test Image',
                    width=1200,
                    height=630)

        self.assertEqual(OgpMediaProperty.objects.count(), 2)
