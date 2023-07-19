from django.test import TestCase

from users.models import CustomUser


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(username="antonio",
                                  email="antonio@gmail.com",
                                  password="pbkdf2_sha256$600000$ukMIjlUV07iN2iDZ1lKFue$p2h68xOopcsuiC35z08Kb2PvspuMzJQqiFbE09FNDZs=")

    def test_email_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
