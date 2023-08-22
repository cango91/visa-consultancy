
from django.test import TestCase
from forms_service.validators.base_validator import ArgumentValidationError, BaseValidator
from forms_service.validators.constraints.min_value import MinValueConstraint
from forms_service.validators.validators import MinLengthValidator, MaxLengthValidator,ValidationError


class ConcreteValidator(BaseValidator):
    def get_expected_args(self):
        return [(int, [MinValueConstraint(5)])]

    def validate(self, value):
        pass

class TestBaseValidator(TestCase):
    def test_init_with_correct_args(self):
        validator = ConcreteValidator(10)
        self.assertEqual(validator.args, (10,))

    def test_init_with_incorrect_type(self):
        with self.assertRaises(TypeError):
            ConcreteValidator("string")

    def test_init_with_constraint_violation(self):
        with self.assertRaises(ArgumentValidationError):
            ConcreteValidator(3)

    def test_init_with_missing_args(self):
        with self.assertRaises(ValueError):
            ConcreteValidator()
            
    def test_serialization(self):
        serialized = ConcreteValidator(5).serialize()
        self.assertTrue(serialized['validator'] == 'ConcreteValidator')

class TestLengthValidators(TestCase):
    def test_min_length_validator_valid(self):
        validator = MinLengthValidator(5)
        self.assertIsNone(validator.validate('Hello'))

    def test_min_length_validator_invalid(self):
        validator = MinLengthValidator(10)
        with self.assertRaises(ValidationError):
            validator.validate('Short')

    def test_max_length_validator_valid(self):
        validator = MaxLengthValidator(5)
        self.assertIsNone(validator.validate('Hello'))

    # Test to catch the bug in MaxLengthValidator
    def test_max_length_validator_invalid(self):
        validator = MaxLengthValidator(3)
        with self.assertRaises(ValidationError):
            validator.validate('Too Long')
            
    def test_serialization(self):
        serialized_min = MinLengthValidator(5).serialize()
        serialized_max = MaxLengthValidator(5).serialize()
        self.assertTrue(serialized_min['arguments']==[5])
        self.assertTrue(serialized_max['arguments']==[5])
        self.assertTrue(serialized_min['validator'] == 'MinLengthValidator')
        self.assertTrue(serialized_max['validator'] == 'MaxLengthValidator')