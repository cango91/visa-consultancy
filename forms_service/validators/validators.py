from .base_validator import BaseValidator
from .constraints.min_value import MinValueConstraint

class ValidationError(Exception):
    """
    Custom exception class for argument validation errors.
    """
    pass

class MinLengthValidator(BaseValidator):
    def __init__(self, min_length=0):
        self.min_length = min_length
        super().__init__(min_length)

    def get_expected_args(self):
        return [(int, [MinValueConstraint(0)])]
    
    def serialize(self):
        base_data = super().serialize()
        base_data.update({
            'arguments': [self.min_length]
        })
        return base_data
        
    def validate(self, value):
        if len(value) < self.min_length:
            raise ValidationError(f"Minimum length must be {self.min_length}, got {len(value)}")
        
class MaxLengthValidator(BaseValidator):
    def __init__(self, max_length=0):
        self.max_length = max_length
        super().__init__(max_length)

    def get_expected_args(self):
        return [(int, [MinValueConstraint(0)])]
    
    def serialize(self):
        base_data = super().serialize()
        base_data.update({
            'arguments': [self.max_length]
        })
        return base_data
        
    def validate(self, value):
        if len(value) > self.max_length:
            raise ValidationError(f"Maximum length must be {self.max_length}, got {len(value)}")
