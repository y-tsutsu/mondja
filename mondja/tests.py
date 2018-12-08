from django.core.management import call_command
from django.shortcuts import resolve_url
from django.test import TestCase
from django.urls import resolve

from . import dumpdata


class UrlResolveTests(TestCase):
    def test_url_dumpdata(self):
        found = resolve('/dumpdata/app/')
        self.assertEqual(found.func, dumpdata.dumpdata_app)

    def test_url_login(self):
        found = resolve('/login/')
        self.assertEqual(found.view_name, 'login')

    def test_url_logout(self):
        found = resolve('/logout/')
        self.assertEqual(found.view_name, 'logout')


class ViewTests(TestCase):
    def test_view_dumpdata(self):
        response = self.client.get(resolve_url('/dumpdata/app/'))
        self.assertEqual(302, response.status_code)

    def test_view_login(self):
        response = self.client.get(resolve_url('/login/'))
        self.assertEqual(200, response.status_code)

    def test_view_logout(self):
        response = self.client.get(resolve_url('/logout/'))
        self.assertEqual(302, response.status_code)


class DatabaseTest(TestCase):
    def test_migrate(self):
        try:
            call_command('makemigrations')
            call_command('migrate')
        except Exception:
            self.assertTrue(False)

    def test_loaddata(self):
        try:
            call_command('loaddata', './backup/auth.json')
            call_command('loaddata', './backup/social_django.json')
            call_command('loaddata', './backup/app.json')
        except Exception:
            self.assertTrue(False)
