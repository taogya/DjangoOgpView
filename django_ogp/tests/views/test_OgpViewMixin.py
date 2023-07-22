from django.test import TestCase
from django_ogp.enums import Determiner, MediaType, OgpType
from django_ogp.models import (OgpBasicProperty, OgpCustomProperty,
                               OgpLocaleMaster, OgpMediaProperty,
                               OgpSiteProperty)
from django_ogp.views import OgpViewMixin


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

        prop = OgpBasicProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    title='Test Site Title',
                    type=OgpType.book,
                    url='http://example.com/',
                    description='This is Test Site.',
                    determiner=Determiner.a)
        prop.locales.add(OgpLocaleMaster.objects.first())
        prop.medias.add(OgpMediaProperty.objects.first())
        OgpCustomProperty.objects\
            .create(site=OgpSiteProperty.objects.first(),
                    type=OgpType.book,
                    url='http://example.com/',
                    property='{"book:author": "Test User", "book:tag": "novel"}')

    def test_ogp_prefix_none(self):
        class TestView(OgpViewMixin):
            pass

        view = TestView()

        self.assertEqual(view.ogp_prefix, '')

    def test_ogp_prefix_ogp_custom_none(self):
        class TestView(OgpViewMixin):
            ogp = OgpBasicProperty.objects.first()

        view = TestView()

        self.assertEqual(view.ogp_prefix, 'book: https://ogp.me/ns/book#')

    def test_ogp_prefix_ogp_none(self):
        class TestView(OgpViewMixin):
            ogp_custom = OgpCustomProperty.objects.first()

        view = TestView()

        self.assertEqual(view.ogp_prefix, 'book: https://ogp.me/ns/book#')

    def test_ogp_prefix(self):
        class TestView(OgpViewMixin):
            ogp = OgpBasicProperty.objects.first()
            ogp_custom = OgpCustomProperty.objects.first()

        view = TestView()

        self.assertEqual(view.ogp_prefix, 'book: https://ogp.me/ns/book#')
