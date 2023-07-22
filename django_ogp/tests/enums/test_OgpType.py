from django.test import TestCase
from django_ogp import enums


class Test(TestCase):

    def test_value(self):
        self.assertEqual(len(enums.OgpType), 12)

    def test_namespace(self):
        expect = [
            'music: https://ogp.me/ns/music#',
            'music: https://ogp.me/ns/music#',
            'music: https://ogp.me/ns/music#',
            'music: https://ogp.me/ns/music#',

            'video: https://ogp.me/ns/video#',
            'video: https://ogp.me/ns/video#',
            'video: https://ogp.me/ns/video#',
            'video: https://ogp.me/ns/video#',

            'article: https://ogp.me/ns/article#',
            'book: https://ogp.me/ns/book#',
            'profile: https://ogp.me/ns/profile#',
            'website: https://ogp.me/ns/website#',
        ]
        for t, e in zip(enums.OgpType, expect):
            self.assertEqual(t.namespace, e)
