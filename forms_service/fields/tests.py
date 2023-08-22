from django.test import TestCase
from .text_field import TextField
from forms_service.validators.validators import MinLengthValidator, MaxLengthValidator

class TextFieldTests(TestCase):
    def test_init_with_valid_values_single_arg(self):
        field = TextField('Your Name')
        self.assertIsNotNone(field)
        
    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            TextField()
    
    def test_init_with_validators(self):
        field = TextField('Your name',validations=[MaxLengthValidator(128),MinLengthValidator(3)])
        self.assertIsNotNone(field)
        self.assertTrue(field.enabled)
        
    def test_serialization(self):
        serialized = TextField('Your name',validations=[MaxLengthValidator(128),MinLengthValidator(3)]).serialize()
        self.assertTrue(serialized['label']=='Your name')
        self.assertTrue(serialized['enabled']==True)
        self.assertTrue(isinstance(serialized['validations'],list))
        self.assertTrue(serialized['type']=='text')
    
    def test_deserialization(self):
        serialized_field = {
            'label': 'Your name', 
            'enabled': True, 
            'validations': [
                {'validator': 'MaxLengthValidator', 'arguments': [128]}, 
                {'validator': 'MinLengthValidator', 'arguments': [3]}
                ],
            'type': 'text'
            }
        field = TextField.deserialize(serialized_field)
        self.assertIsNotNone(field)
        self.assertEqual(field.serialize(),serialized_field)