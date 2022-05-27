from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    requirements = models.CharField(max_length=30)
    
    def __str__(self):
        return self.description