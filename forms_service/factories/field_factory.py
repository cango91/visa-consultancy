from forms_service.fields.text_field import TextField

class FieldFactory:
    @staticmethod
    def create_field(field_type, **kwargs):
        field_classes = {
            "text": TextField,
            # Additional field types can be mapped here
        }

        field_class = field_classes.get(field_type.lower())
        if not field_class:
            raise ValueError(f"Invalid field type: {field_type}")

        return field_class(**kwargs)