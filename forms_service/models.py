from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class FormDefinition(models.Model):
    version = models.IntegerField("Form Version")
    definition = models.JSONField("Form Definition")
    translations = models.JSONField()
    default_lang_code = models.CharField(max_length=10, default="en")
    FORM_STATUS = (('draft','Draft'),
                   ('active','Active'),
                   ('inactive','Inactive'),
                   ('decommissioned','Decommissioned'),
                   ('archived','Archived'),
                   ('rejected','Rejected'),
                   ('pending_approval','Pending Approval'),
                   ('deleted','Deleted'))
    status = models.CharField(max_length=25,choices=FORM_STATUS)
    created_at = models.DateTimeField("Created At",default=timezone.now)
    created_by = models.OneToOneField(get_user_model(),on_delete=models.DO_NOTHING,null=True)
    
    def __str__(self) -> str:
        return f"{self.status} form created by {self.created_by.name} @ {self.created_at}"
    
class FormSubmission(models.Model):
    form_id = models.ForeignKey(FormDefinition, on_delete=models.CASCADE, related_name='form_submissions')
    submitted_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(default=timezone.now)
    data = models.JSONField()
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"Form data submitted by {self.submitted_by.name} @ {self.submitted_at}, for form id: {self.form_id.pk}"