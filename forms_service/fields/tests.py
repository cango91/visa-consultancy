from django.test import TestCase

from forms_service.fields.select_field import SelectField
from .text_field import TextField
from forms_service.validators.validators import MinLengthValidator, MaxLengthValidator
from forms_service.factories.validator_factory import ValidatorFactory

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
        
    def test_deserialization_without_validations(self):
        serialized_field = {
            'label': 'Your name', 
            'enabled': True, 
            'validations': [],
            'type': 'text'
            }
        field2 = TextField('Your name')
        field = TextField.deserialize(serialized_field)
        self.assertIsNotNone(field)
        self.assertEqual(field.serialize(),serialized_field)
        self.assertEqual(field2.serialize(),serialized_field)
        
        
        
class SelectFieldTest(TestCase):
    def test_serialization_and_deserialization(self):
        options = [
            {'label': 'Option 1', 'value': 'value1'},
            {'label': 'Option 2', 'value': 'value2', 'enables': 'value3'},
        ]
        validations = [ValidatorFactory.create_validator({'validator': 'MinLengthValidator', 'arguments': [1]})]

        select_field = SelectField(label="Test Select Field", options=options, enabled=True, validations=validations)
        
        # Test Serialization
        serialized_data = select_field.serialize()
        expected_serialized_data = {
            "label": "Test Select Field",
            "enabled": True,
            "validations": [validation.serialize() for validation in validations],
            "type": "select",
            "options": options
        }
        self.assertEqual(serialized_data, expected_serialized_data)

        # Test Deserialization
        deserialized_field = SelectField.deserialize(serialized_data)
        self.assertEqual(deserialized_field.label, "Test Select Field")
        self.assertEqual(deserialized_field.enabled, True)
        self.assertEqual(deserialized_field.options, options)
    
    def test_invalid_options_init(self):
        with self.assertRaises(ValueError):
            SelectField("label",5)
        with self.assertRaises(ValueError):
            SelectField("label", [{'label':'This choice'}])
        with self.assertRaises(TypeError):
            SelectField("label", [{'label':'label1','value':5}])
        with self.assertRaises(TypeError):
            SelectField("label",[{'label':'label2','value':'value1','enables':True}])
            