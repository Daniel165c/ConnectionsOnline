from django.db import models


class Job (models.Model):
    job_title = models.CharField(max_length=30)
    job_descriptions = models.CharField(max_length=30)
    job_requirements = models.CharField(max_length=30)