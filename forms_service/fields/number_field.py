from .base_field import BaseField
from forms_service.factories.validator_factory import ValidatorFactory

class NumberField(BaseField):
    def __init__(self, label, enabled=True, validations=None):
        super().__init__(label, enabled, validations)
        
    def serialize(self):
        """
        Serializes the text field into a JSON-compatible format.
        """
        base_data = super().serialize()
        base_data.update({"type": "number"})
        return base_data
    
    @staticmethod
    def deserialize(json_data):
        return NumberField(
            label=json_data['label'],
            enabled=json_data['enabled'],
            validations=[ValidatorFactory.create_validator(v) for v in json_data['validations']]
        )