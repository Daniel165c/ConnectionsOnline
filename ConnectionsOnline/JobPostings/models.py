from django.db import models

class Jobs(models.Model):
    job_title = models.CharField(max_length=30, null=True, blank=True)
    job_description = models.CharField(max_length=250, null=True, blank=True)