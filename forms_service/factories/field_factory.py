from forms_service.fields import TextField, NumberField, SelectField

class FieldFactory:
    
    FIELD_CLASSES = {
        "text": TextField,
        "number": NumberField,
        "select": SelectField,
    }
    
    FIELD_INFO = {
        "text": {
            "validators": ["MinLengthValidator","MaxLengthValidator","RequiredValidator"],
            "extra_attributes": [],
        },
        "number": {
            "validators": ["MinValueValidator","MaxValueValidator","RequiredValidator"],
            "extra_attributes": [],
        },
        "select":{
            "validators": [],
            "extra_attributes": [{"options":"list of dictionaries with required `label` and `value` keys. Optional `enables` key. All values must be strings"}]
        }
    }    
    
    @staticmethod
    def create_field(field_type, **kwargs):
        field_class = FieldFactory.FIELD_CLASSES.get(field_type.lower())
        if not field_class:
            raise ValueError(f"Invalid field type: {field_type}")

        return field_class(**kwargs)