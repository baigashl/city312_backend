import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import ActivityType, Category

client = APIClient()

# Activity Type Tests


class AccountAPITests(APITestCase):

    def test_list(self):
        url = reverse('activity_type_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = reverse('activity_type_create')
        data = {"name": "asd"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        self.casper = ActivityType.objects.create(
            name='Casper')
        self.muffin = ActivityType.objects.create(
            name='Muffy')
        self.valid_payload = {
            'name': 'Muffy',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_detail(self):
        url = reverse('activity_type_detail', kwargs={'id': self.muffin.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = client.delete(
            reverse('activity_type_detail', kwargs={'id': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        response = client.put(
            reverse('activity_type_detail', kwargs={'id': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Category Tests

class CategoryAPITests(APITestCase):
    def test_list(self):
        url = reverse('category_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def setUp(self):
        self.casper = ActivityType.objects.create(
            name='Casper')
        self.muffin = Category.objects.create(
            activity_type_id=1, name='Muffy')
        self.valid_payload = {
            'activity_type_id': 1,
            'name': 'Muffy',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_create(self):
        url = reverse('category_create')
        data = {"name": "asd", "activity_type": 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail(self):
        url = reverse('category_detail', kwargs={'id': self.muffin.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = client.delete(
            reverse('category_detail', kwargs={'id': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        response = client.options(
            reverse('category_detail', kwargs={'id': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
