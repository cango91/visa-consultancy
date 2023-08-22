from .base_field import BaseField

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