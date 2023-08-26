from abc import ABC, abstractmethod


class BaseField(ABC):
    def __init__(self, label, order, section=None, enabled=True, validations=None,help_info=None):
        self.label = label
        self.enabled = enabled
        self.validations = validations or []
        self.help_info = help_info
        self.order = order
        self.section = section
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
        serialized = {
            "label": self.label,
            "enabled": self.enabled,
            "validations": [validation.serialize() for validation in self.validations]
        }
        if self.help_info:
            serialized.update({"help_info":self.help_info})
        return serialized
        
    @staticmethod
    @abstractmethod
    def deserialize(json_data):
        """
        Deserializes the given JSON data into a field object.
        Must be implemented by the concrete field classes.
        """
        pass


class FieldValidationError(Exception):
    """
    Custom exception class for field validation errors.
    """
    pass
