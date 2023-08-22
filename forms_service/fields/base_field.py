from abc import ABC, abstractmethod


class BaseField(ABC):
    def __init__(self, label, enabled=True, validations=None):
        self.label = label
        self.enabled = enabled
        self.validations = validations or []
        self.validate_field()

    @abstractmethod
    def validate_field(self):
        """
        Validates the field's specific properties and raises appropriate errors if invalid.
        Must be implemented by the concrete field type classes.
        """
        pass

    def add_validation(self, validation):
        self.validations.append(validation)

    def remove_validation(self, validation):
        self.validations.remove(validation)

    def validate(self, value):
        """
        Validates the given value using the associated validation strategies.
        """
        if not self.enabled:
            raise FieldValidationError("Field is not enabled.")

        for validation in self.validations:
            validation.validate(value)

    def serialize(self):
        """
        Serializes the field into a JSON-compatible format.
        """
        return {
            "label": self.label,
            "enabled": self.enabled,
            "validations": [validation.serialize() for validation in self.validations]
        }


class FieldValidationError(Exception):
    """
    Custom exception class for field validation errors.
    """
    pass
