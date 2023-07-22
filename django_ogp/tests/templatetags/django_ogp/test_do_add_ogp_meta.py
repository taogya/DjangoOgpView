
from django.test import TestCase
from django.views import View
from django_ogp.models import OgpBasicProperty, OgpCustomProperty
from django_ogp.templatetags.django_ogp import do_add_ogp_meta


class Test(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()

    def test_not_hasattr(self):

        res = do_add_ogp_meta({})

        self.assertEqual(res, {'ogp': None, 'ogp_custom': None})

    def test_hasattr(self):
        class TestView(View):
            ogp = OgpBasicProperty()
            ogp_custom = OgpCustomProperty()

        view = TestView()
        res = do_add_ogp_meta({'view': view})

        self.assertEqual(res, {'ogp': view.ogp, 'ogp_custom': view.ogp_custom})
