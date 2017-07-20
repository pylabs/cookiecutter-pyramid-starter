import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from .views import home_view
        request = testing.DummyRequest()
        info = home_view(request)
        self.assertEqual(info['project'], '{{ cookiecutter.project_name }}')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from {{ cookiecutter.repo_name }} import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'{{ cookiecutter.project_name }}' in res.body)
