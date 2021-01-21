from unittest import TestCase
from app import app
from flask import session
from converter import Converter
forex_conversion = Converter()

"""test if the template renders correctly"""

class ConverterTest(TestCase):

    def setUp(self):
        self.client = app.test_client()


    def test_form_renders(self):
        """Test that form appears"""

        resp = self.client.get('/')

        self.assertIn(b'<form', resp.data)
