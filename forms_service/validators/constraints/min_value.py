from .base_constraint import BaseConstraint

class MinValueConstraint(BaseConstraint):
    def __init__(self, min_value) -> None:
        if min_value is None: raise ValueError("min_value must be provided")
        self.min_value = min_value
        super().__init__()
        
    def validate(self, value):
        return value >= self.min_value
    def error_message(self):
        return f"Minimum value can be: {self.min_value}"