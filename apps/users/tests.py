from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from .models import User, Partner
from django.urls import reverse
import json
from rest_framework import status
from apps.activity_type.models import ActivityType
import tempfile

from PIL import Image as ImageFile, Image

client = Client()


class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = User.objects.create(
            email='normal@users.com',
            name='foo',
            second_name='asd',
            date_of_birth='12/12/12',
            phone_number='123123123',
            discount_card_number='123123123',
            contract_offer='123123123123',
            isPartner=False,
            is_admin=False
        )
        user.set_password('islamSmart1!')
        self.assertEqual(user.email, 'normal@users.com')
        self.assertEqual(user.name, 'foo')
        self.assertEqual(user.second_name, 'asd')
        self.assertEqual(user.date_of_birth, '12/12/12')
        self.assertEqual(user.phone_number, '123123123')
        self.assertEqual(user.discount_card_number, '123123123')
        self.assertEqual(user.contract_offer, '123123123123')
        self.assertFalse(user.is_admin)
        self.assertFalse(user.isPartner)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo!")

    # def test_create_superuser(self):
    #     User = get_user_model()
    #     admin_user = User.objects.create_superuser('super@users.com', 'foo')
    #     self.assertEqual(admin_user.email, 'super@users.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(admin_user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(ValueError):
    #         User.objects.create_superuser(
    #             email='super@users.com', password='foo', is_superuser=False)


class RegisterPartnerTest(TestCase):
    """ Test module for updating an existing puppy record """

    def generate_img(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        return tmp_file.seek(0)

    def setUp(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        self.activity_type = ActivityType.objects.create(
            name='Casper')
        self.partner = Partner.objects.create(
            email='normal@users.com',
            activity_type=self.activity_type,
            brand_name='asd',
            organization_form='456456456876',
            phone_number='123123123',
            description='jhgfjhgfjhgf',
            inn='123123123123',
            isVip=False,
            isPartner=True,
            is_admin=False
        )

        self.valid_partner = {
            'email': 'normal@users.com',
            'activity_type': 1,
            'brand_name': 'asd',
            'organization_form': '456456456876',
            'phone_number': '123123123',
            'description': 'jhgfjhgfjhgf',
            'inn': '123123123123',
            'logo': tmp_file,
            'isVip': True,
            'isPartner': True,
            'is_admin': False
        }
        self.invalid_partner = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_register_partner(self):
        response = client.post(
            reverse('register-partner'),
            data=json.dumps(self.valid_partner),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_partner(self):
        response = client.get(
            reverse('partner-list'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_update_partner(self):
        response = client.put(
            reverse('partner-detail', kwargs={'id': self.partner.pk}),
            data=json.dumps(self.valid_partner),
            content_type='multipart/form-data'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_partner(self):
        response = client.put(
            reverse('partner-detail', kwargs={'id': self.partner.pk}),
            data=json.dumps(self.invalid_partner),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_partner(self):
        response = client.delete(
            reverse('partner-detail', kwargs={'id': self.partner.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
