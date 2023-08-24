from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class WorkflowStep(models.Model):
    name = models.CharField(max_length=50)
    workflow = models.ForeignKey('Workflow',on_delete=models.CASCADE,related_name="steps")
    leads_to = models.ManyToManyField('self',symmetrical=False,blank=True,related_name="leading_steps")
    
class Workflow(models.Model):
    job_type = models.OneToOneField('JobType',on_delete=models.CASCADE)

class JobStatus(models.Model):
    name = models.CharField(max_length=50)
    workflow = models.ManyToManyField(Workflow,related_name="available_statuses")

class JobType(models.Model):
    name = models.CharField(max_length=25)
    JOB_TYPE_STATUS = (('active','Active'),
                       ('inactive','Inactive'))
    status = models.CharField(max_length=25,choices=JOB_TYPE_STATUS)
    
class Job(models.Model):
    job_type = models.ForeignKey(JobType,on_delete=models.DO_NOTHING,null=True,blank=
                                 False)
    customer = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING,null=True,blank=False)
    assignee = models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING,null=True,blank=True)
    invoice = models.ForeignKey('Invoice', on_delete= models.PROTECT)
    unique_id = models.CharField(max_length=128,unique=True)
    # JOB_STATUS = (('pending_assignment','Pending Assignment to Employee'),
    #               ('assigned','Assigned to Employee'),
    #               ('pending_review','Pending Review'),
    #               ('pending_resubmission','Pending Resubmission for Missing Information or Document(s)'),
    #               ('application_submitted'))
    # status = models.CharField(max_length=25)
    status = models.ForeignKey(JobStatus,on_delete=models.PROTECT)
    