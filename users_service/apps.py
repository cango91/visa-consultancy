from django.apps import AppConfig


class UsersServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_service'
    
    def ready(self):
        from . import signals
