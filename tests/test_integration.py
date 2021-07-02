from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from datastore.models import DataStore


class IntegrationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.url = reverse('datastore:datastore-detail', args=['some_key'])
        self.client._login(self.user)

    def test_get_does_not_exist(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_put_does_not_exist(self):
        response = self.client.put(self.url, data={'hej': {'hej': 'då'}}, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'hej': {'hej': 'då'}})

    def test_get_does_exist(self):
        DataStore.objects.create(user=self.user, key='some_key', data={'hej': 'alla'})

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'hej': 'alla'})

    def test_put_does_exist(self):
        DataStore.objects.create(user=self.user, key='some_key', data={'hej': 'alla'})

        response = self.client.put(self.url, data={'hej': {'hej': 'då'}}, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'hej': {'hej': 'då'}})

    def test_put_different_key(self):
        DataStore.objects.create(user=self.user, key='some_other_key', data={'hej': 'alla'})

        response = self.client.put(self.url, data={'hej': {'hej': 'då'}}, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'hej': {'hej': 'då'}})
        self.assertEqual(DataStore.objects.count(), 2)

    def test_correct_stored_values(self):
        response = self.client.put(self.url, data={'hej': {'hej': 'då'}}, content_type='application/json')

        ds = DataStore.objects.last()

        self.assertEqual(ds.key, 'some_key')
        self.assertEqual(ds.user, self.user)
        self.assertEqual(ds.data, {'hej': {'hej': 'då'}})

    def test_permissions(self):
        self.client.logout()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})
