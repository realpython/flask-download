# tests/test_forms.py


import unittest

from base import BaseTestCase
from project.user.forms import LoginForm


class TestLoginForm(BaseTestCase):

    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(email='ad@min.com', password='admin_user')
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Ensure invalid email format throws error.
        form = LoginForm(email='unknown', password='example')
        self.assertFalse(form.validate())


if __name__ == '__main__':
    unittest.main()
