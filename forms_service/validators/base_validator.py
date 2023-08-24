from abc import ABC, abstractmethod

class BaseValidator(ABC):
    def __init__(self, *args):
        self.expected_args = self.get_expected_args()
        self.validate_args(*args)
        self.args = args
        
    @abstractmethod
    def get_expected_args(self):
        """
        Returns a list of tuples defining the expected arguments for this validator.
        Each tuple should contain the type and any additional constraints as an array.
        If no constraints are necessary, an empty array should be passed as second element of tuple
        Must be implemented by the concrete validator classes.
        """
        pass
    
    def validate_args(self, *args):
        if len(args) != len(self.expected_args):
            raise ValueError("Argument count mismatch.")

        for arg, (expected_type, constraints) in zip(args, self.expected_args):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Expected argument of type {expected_type}, got {type(arg)}.")

            if constraints and len(constraints):
                for constraint in constraints:
                    if not constraint.validate(arg):
                        raise ArgumentValidationError(f"Argument does not meet required constraint: {constraint.error_message()}")

    
    @abstractmethod
    def validate(self, value):
        """
        Validates the given value and raises an exception if invalid.
        Must be implemented by the concrete validator classes.
        """
        pass

    def serialize(self):
        """
        Serializes the validator into a JSON-compatible format.
        This can be overridden by concrete classes if additional properties are required.
        """
        return {
            "validator": self.__class__.__name__
        }
        
class ArgumentValidationError(Exception):
    """
    Custom exception class for argument validation errors.
    """
    pass