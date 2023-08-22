from fields.text_field import TextField

class FieldFactory:
    def create_field(self, field_type, **kwargs):
        field_classes = {
            "text": TextField,
            # Additional field types can be mapped here
        }

        field_class = field_classes.get(field_type)
        if not field_class:
            raise ValueError(f"Invalid field type: {field_type}")

        return field_class(**kwargs)