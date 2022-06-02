from django.db import models

# Create your models here.


class Job (models.model):
    job_title = models.CharField(max_length=30)
    job_descriptions = models.CharField(max_length=30)
    job_requirements = models.CharField(max_length=30)