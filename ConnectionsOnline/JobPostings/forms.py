from django import forms
from .models import Job

class JobListingForm(forms.Form):
    JobTitle = forms.CharField(label='Post Job', max_length=255)