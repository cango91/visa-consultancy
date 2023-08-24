from django.apps import AppConfig


class FormsServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forms_service'

    def ready(self):
        from . import signals