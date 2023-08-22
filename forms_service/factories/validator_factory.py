from forms_service.validators.validators import MinLengthValidator, MaxLengthValidator

class ValidatorFactory:
    @staticmethod
    def create_validator(validator_data):
        validator_name = validator_data['validator']
        validator_args = validator_data.get('arguments', [])
        
        # Mapping of validator names to their respective classes
        validator_classes = {
            'MinLengthValidator': MinLengthValidator,
            'MaxLengthValidator': MaxLengthValidator,
            # Add other concrete validator classes here
        }

        validator_class = validator_classes.get(validator_name)
        if not validator_class:
            raise ValueError(f"Invalid validator name: {validator_name}")

        return validator_class(*validator_args)