from forms_service.validators.validators import StringEnumValidator
from .base_field import BaseField
from forms_service.factories.validator_factory import ValidatorFactory

class SelectField(BaseField):
    def __init__(self, label, options, enabled=True, validations=None, create_implicit_validator=True):
        self.options = options
        super().__init__(label, enabled, validations)
        if(create_implicit_validator):
            self.add_validation(StringEnumValidator([option["value"] for option in self.options]))
        
    def validate_field(self):
        """
        Validates the options passed in constructor. It must be a list of dictionaries. Every item in the dictionary must have label and value strings. Optionally they may have an enables string.
        """
        super().validate_field()
        if not isinstance(self.options, list) or not all(isinstance(option, dict) for option in self.options):
            raise ValueError("Options must be a list of dictionaries.")

        for option in self.options:
            label = option.get('label')
            value = option.get('value')
            if label is None or value is None:
                raise ValueError("Both 'label' and 'value' must be provided in options.")

            if not isinstance(label, str) or not isinstance(value, str):
                raise TypeError("'label' and 'value' in options must be of type string.")

            # If 'enables' is present, it must also be a string
            enables = option.get('enables')
            if enables and not isinstance(enables, str):
                raise TypeError("'enables' in options must be of type string if provided.")
        
    def serialize(self):
        """
        Serializes the select field into a JSON-compatible format.
        """
        base_data = super().serialize()
        base_data.update({"type": "select",
                          'options': [
                              {'label': option['label'], 'value': option['value'], 'enables': option['enables'] }
                              if option.get('enables')
                              else 
                              {'label': option['label'], 'value': option['value']} 
                              for option in self.options]
                          })
        return base_data
    
    @staticmethod
    def deserialize(json_data, create_implicit_validator = False):
        """
        When deserializing from client submitted definition, pass True to create_implicit_validator flag. This ensures that an implicit validator is saved in the database instance. When deserializing db retrieved definition, be sure to keep it False so as not to add multiple instances.
        """
        return SelectField(
            label=json_data['label'],
            enabled=json_data['enabled'],
            options = [
                {'label': option['label'], 'value': option['value'], 'enables': option['enables'] } 
                if option.get('enables') 
                else 
                {'label': option['label'], 'value': option['value']} 
                for option in json_data['options']
                ],
            validations=[ValidatorFactory.create_validator(v) for v in json_data['validations']],
            create_implicit_validator = create_implicit_validator
        )