
from django.db import transaction
from django.test import TestCase
from django_ogp.enums import Determiner, MediaType, OgpType
from django_ogp.models import (OgpBasicProperty, OgpLocaleMaster,
                               OgpMediaProperty, OgpSiteProperty)


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        OgpSiteProperty.objects\
            .create(name='Test Site')
        OgpMediaProperty.objects\
            .create(media_type=MediaType.image,
                    url='http://example.com/static/image/test.png',
                    secure_url='https://example.com/static/image/test.png',
                    type_id='image/png',
                    alt='Test Image',
                    width=1200,
                    height=630)

    def test_empty(self):
        from django.db.utils import IntegrityError

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                OgpBasicProperty.objects.create()
        self.assertEqual(OgpBasicProperty.objects.count(), 0)

        # フォームからの入力の場合は、['title', 'type', 'url', 'description']の空文字を許容しない。
        OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.website,
                    url='http://example.com/',
                    description='This is Test Site.')
        self.assertEqual(OgpMediaProperty.objects.count(), 1)

    def test_create(self):
        prop = OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.website,
                    url='http://example.com/',
                    description='This is Test Site.',
                    determiner=Determiner.a)
        prop.locales.add(OgpLocaleMaster.objects.first())
        prop.medias.add(OgpMediaProperty.objects.first())

        self.assertEqual(OgpBasicProperty.objects.count(), 1)
        self.assertEqual(OgpBasicProperty.objects.first().locales.count(), 1)
        self.assertEqual(OgpBasicProperty.objects.first().medias.count(), 1)

    def test_duplicate(self):
        prop = OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.website,
                    url='http://example.com/',
                    description='This is Test Site.',
                    determiner=Determiner.a)
        prop.locales.add(OgpLocaleMaster.objects.first())
        prop.medias.add(OgpMediaProperty.objects.first())
        prop = OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.website,
                    url='http://example.com/',
                    description='This is Test Site.',
                    determiner=Determiner.a)
        prop.locales.add(OgpLocaleMaster.objects.first())
        prop.medias.add(OgpMediaProperty.objects.first())

        self.assertEqual(OgpBasicProperty.objects.count(), 2)
        self.assertEqual(OgpBasicProperty.objects.first().locales.count(), 1)
        self.assertEqual(OgpBasicProperty.objects.first().medias.count(), 1)

    def test_reverse(self):
        prop = OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.website,
                    url='http://example.com/',
                    description='This is Test Site.',
                    determiner=Determiner.a)
        prop.locales.add(OgpLocaleMaster.objects.first())
        prop.medias.add(OgpMediaProperty.objects.first())

        self.assertEqual(OgpLocaleMaster.objects.first().basics.count(), 1)
        self.assertEqual(OgpMediaProperty.objects.first().basics.count(), 1)
