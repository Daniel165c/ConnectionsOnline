from django import forms
from django.forms import ModelForm
from .models import Job

class JobListingForm(ModelForm):
   class Meta:
        JobTitle= forms.CharField(label='Job Title', max_length=255)
        JobDescription = forms.CharField(widget=forms.Textarea, label='Job Description')