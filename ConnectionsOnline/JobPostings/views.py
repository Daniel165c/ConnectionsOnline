from django.shortcuts import render, redirect
from django.views import View
from .models import Job
from JobPostings.forms import JobListingForm
# from paintapp.forms import ColorPickerForm

# Create your views here.

class ConnectionsOnlineView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')

class PostJobsViews(View):
    def get(self, request):
        form = JobListingForm()  
        return render(request=request,
        template_name='postjobs.html',context = {'form': form})

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form = JobListingForm (request.POST)
        if form.is_valid():
          description = form.cleaned_data['JobTitle']
          Job.objects.create(job_description=description)

        # "redirect" to the postjob homepage
        return redirect('postjobs')  