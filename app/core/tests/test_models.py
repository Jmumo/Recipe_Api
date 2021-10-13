from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """creating a new user with an email"""
        testEmail = 'john@pythonrest.com'
        testpassword = 'testpassword123'

        user = get_user_model().objects.create_user(
            email = testEmail,
            password = testpassword
        )
        self.assertEqual(user.email, testEmail)
        self.assertTrue(user.check_password(testpassword))

    def test_user_email_is_nomarlized(self):
        """check if user email is normalised"""

        email = "john@JAY.com"
        password ='test123'
        
        user = get_user_model().objects.create_user(email,password)

        self.assertEqual(user.email,email.lower())

    def test_user_email_is_provided(self):
        """test if email is provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test1234')

    def test_create_super_user(self):
        email = 'super@user.com'
        password = 'testsuper234'

        user = get_user_model().objects.create_super_user(email,password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
