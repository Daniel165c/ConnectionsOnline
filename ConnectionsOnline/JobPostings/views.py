from turtle import title
from django.shortcuts import render, redirect
from django.views import View
from JobPostings.models import Job
from JobPostings.forms import *

class ConnectionsOnlineView(View):
    def get(self,request):
        return render(request=request, template_name='home.html')

class PostJobsView(View):
    def get(self, request):
        job = Job.objects.all().order_by('id')
        form = JobListingForm() 
        return render(request=request,
        template_name='postjobs.html',context = {'id': job, 'form': form})

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form = JobListingForm(request.POST)
        if form.is_valid():
        #   title = form.cleaned_data['JobTitle']
          description = form.cleaned_data['JobDescription']
          Job.objects.create(description=description)
        print(request, description) 
        # "redirect" to the postjob homepage
        return redirect('postjobs')  

class JobListingsView(View):
    def get(self, request):
        form = JobListingForm() 
        print(request) 
        return render(request=request,
        template_name='joblist.html',context = {'form': form})

    def post(self, request):
        '''POST the data in the from submitted by the user, creating a new task in the todo list'''
        form = JobListingForm (request.POST)
        if form.is_valid():
          title = form.cleaned_data['JobTitle']
          Job.objects.create(title=title)

        # "redirect" to the postjob homepage
        return redirect('joblist')  
        