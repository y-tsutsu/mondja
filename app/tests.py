from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import resolve_url
from . import views


class UrlResolveTests(TestCase):
    def test_url_home(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home)

    def test_url_add(self):
        found = resolve('/add/')
        self.assertEqual(found.func, views.add_memo)

    def test_url_edit(self):
        found = resolve('/edit/42/')
        self.assertEqual(found.func, views.edit_memo)

    def test_url_delete(self):
        found = resolve('/delete/42/')
        self.assertEqual(found.func, views.delete_memo)

    def test_url_refresh(self):
        found = resolve('/refresh/')
        self.assertEqual(found.func, views.refresh_memo)


class ViewTests(TestCase):
    def test_view_home(self):
        response = self.client.get(resolve_url('/'))
        self.assertEqual(302, response.status_code)

    def test_url_add(self):
        response = self.client.get(resolve_url('/add/'))
        self.assertEqual(302, response.status_code)

    def test_url_edit(self):
        response = self.client.get(resolve_url('/edit/42/'))
        self.assertEqual(302, response.status_code)

    def test_url_delete(self):
        response = self.client.get(resolve_url('/delete/42/'))
        self.assertEqual(302, response.status_code)

    def test_url_refresh(self):
        response = self.client.get(resolve_url('/refresh/'))
        self.assertEqual(302, response.status_code)
