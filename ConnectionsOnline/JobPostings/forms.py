from django import forms

class JobListingForm(forms.Form):
    JobTitle= forms.CharField(label='Job Title', max_length=255)
    JobDescription = forms.CharField(widget=forms.Textarea, label='Job Description')