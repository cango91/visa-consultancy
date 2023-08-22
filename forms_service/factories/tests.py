from django.test import TestCase
from .field_factory import FieldFactory
from forms_service.fields.text_field import TextField
from forms_service.validators.validators import MaxLengthValidator

class FieldFactoryTests(TestCase):
    def test_text_field_factory(self):
        field = FieldFactory.create_field('text',label="Your name", validations=[MaxLengthValidator(128)])
        field2 = TextField("Your name",validations=[MaxLengthValidator(128)])
        self.assertIsNotNone(field)
        self.assertEqual(field.serialize(),field2.serialize())