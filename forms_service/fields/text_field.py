from .base_field import BaseField
from forms_service.factories.validator_factory import ValidatorFactory

class TextField(BaseField):
    def __init__(self, label, enabled=True, validations=None):
        super().__init__(label, enabled, validations)
        
    def validate_field(self):
        """
        Any specific validation for the text field can be done here.
        Currently, no specific validations are required.
        """
        pass
    
    def serialize(self):
        """
        Serializes the text field into a JSON-compatible format.
        """
        base_data = super().serialize()
        base_data.update({"type": "text"})
        return base_data
    
    @staticmethod
    def deserialize(json_data):
        return TextField(
            label=json_data['label'],
            enabled=json_data['enabled'],
            validations=[ValidatorFactory.create_validator(v) for v in json_data['validations']]
        )