from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models import ProtectedError
from django.contrib.auth import get_user_model
from .models import FormDefinition

@receiver(pre_delete,sender = get_user_model())
def handle_user_deletion(sender,instance,**kwargs):
    FormDefinition.objects.filter(created_by=instance,form_submissions__isnull=False).update(status='deleted', created_by=None)
    FormDefinition.objects.filter(created_by=instance, form_submissions__isnull=True).delete()