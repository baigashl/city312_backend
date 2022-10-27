from django.test import TestCase, Client
from .models import User, Partner
from django.urls import reverse
import json
from rest_framework import status

client = Client()


class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = User.objects.create(
            email='normal@users.com',
            password='foo',
            brand_name='asd',
            organization_form='asdasd',
            phone_number='123123123',
            description='asd',
            inn='asd',
            isVip=True,
            transaction_quantity=0,
            isPartner=True
        )
        self.assertEqual(user.email, 'normal@users.com')
        self.assertEqual(user.brand_name, 'asd')
        self.assertEqual(user.organization_form, 'asdasd')
        self.assertEqual(user.phone_number, '123123123')
        self.assertEqual(user.description, 'asd')
        self.assertEqual(user.inn, 'asd')
        self.assertEqual(user.transaction_quantity, 0)
        self.assertTrue(user.isVip)
        self.assertTrue(user.isPartner)
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
            User.objects.create_user(email='', password="foo")

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


# class RegisterPartnerTest(TestCase):
#     """ Test module for updating an existing puppy record """
#
#     def setUp(self):
#         self.casper = Partner.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')
#         self.muffin = Partner.objects.create(
#             name='Muffy', age=1, breed='Gradane', color='Brown')
#         self.valid_payload = {
#             'name': 'Muffy',
#             'age': 2,
#             'breed': 'Labrador',
#             'color': 'Black'
#         }
#         self.invalid_payload = {
#             'name': '',
#             'age': 4,
#             'breed': 'Pamerion',
#             'color': 'White'
#         }
#
#     def test_valid_update_puppy(self):
#         response = client.put(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_invalid_update_puppy(self):
#         response = client.put(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
