from django.test import TestCase
# from .models import CustomUser
#
#
# class UsersManagersTests(TestCase):
#
#     def test_create_user(self):
#         User = CustomUser
#         user = CustomUser.objects.create(
#             email='normal@users.com',
#             password='foo',
#             brand_name='asd',
#             organization_form='asdasd',
#             phone_number='123123123',
#             description='asd',
#             inn='asd',
#             isVip=True,
#             transaction_quantity=0,
#             isPartner=True
#         )
#         self.assertEqual(user.email, 'normal@users.com')
#         self.assertEqual(user.brand_name, 'asd')
#         self.assertEqual(user.organization_form, 'asdasd')
#         self.assertEqual(user.phone_number, '123123123')
#         self.assertEqual(user.description, 'asd')
#         self.assertEqual(user.inn, 'asd')
#         self.assertEqual(user.transaction_quantity, 0)
#         self.assertTrue(user.isVip)
#         self.assertTrue(user.isPartner)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email='', password="foo")

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
