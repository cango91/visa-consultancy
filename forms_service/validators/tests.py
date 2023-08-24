
from django.test import TestCase
from forms_service.validators.base_validator import ArgumentValidationError, BaseValidator
from forms_service.validators.constraints.min_value import MinValueConstraint
from forms_service.validators.validators import EnumValidator, MinLengthValidator, MaxLengthValidator, RequiredValidator,ValidationError


class ConcreteValidator(BaseValidator):
    def get_expected_args(self):
        return [(int, [MinValueConstraint(5)])]

    def validate(self, value):
        pass

## BaseValidator tests ##
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

## Min/MaxLengthValidator tests ##
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
        
## RequiredValidator Tests ##
class TestRequiredValidator(TestCase):
    def test_raises_on_empty_value(self):
        with self.assertRaises(ValidationError):
            RequiredValidator().validate("")
            
    def test_raises_on_whitespace(self):
        with self.assertRaises(ValidationError):
            RequiredValidator().validate("    ")
            
    def test_raises_on_linebreaks(self):
        with self.assertRaises(ValidationError):
            RequiredValidator().validate("""
                                         """)
    def test_raises_on_none(self):
        with self.assertRaises(ValidationError):
            RequiredValidator().validate(None)
            
    def test_passes_non_empty_string(self):
        self.assertIsNone(RequiredValidator().validate("non-empty"))
        
    def test_passes_number_zero(self):
        self.assertIsNone(RequiredValidator().validate(0))
        
            
    def test_passes_bool_false(self):
        self.assertIsNone(RequiredValidator().validate(False))
        
## EnumValidator Tests ##
class TestEnumValidator(TestCase):
    def test_init_with_list(self):
        self.assertIsNotNone(EnumValidator(["first",2,'third']))
        
    def test_init_with_empty_list(self):
        with self.assertRaises(ValueError):
            EnumValidator([])
            
    def test_value_in_enum_passes_test(self):
        self.assertIsNone(EnumValidator([1,2,3]).validate(1))
        self.assertIsNone(EnumValidator(["a","b"]).validate("b"))
        
    def test_value_outside_enum_fails_test(self):
        with self.assertRaises(ValidationError):
            EnumValidator([1,2,3]).validate(4)
        with self.assertRaises(ValidationError):
            EnumValidator([1,2,3]).validate("1")