from django.test import TestCase
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse

# Практическая 16

class TestCaseViewAccount(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'тесткейс',
            'email': '0-zh@mail.ru',
            'password1': 'Qol:54hgf#',
            'password2': 'Qol:54hgf#'
        }

    def test_register_view(self):
        RegisterForm(data=self.form_data)
        self.client.post(reverse('register'), data=self.form_data)
        print(self.form_data['username'])
        user = User.objects.filter(username=self.form_data['username']).exists()
        self.assertTrue(user)