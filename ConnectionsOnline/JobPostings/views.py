from unittest import skip
from django.shortcuts import render
from django.views import View
from JobPostings.models import Jobs
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
class ConnectionsOnlineView(View):
    def get(self, request):
        return render(request,'home.html')
class ConnectionsOnlineUpdateView(View):
    def get(self, request, id):
        job_to_update = Jobs.objects.get(id=id)
        context = {
            'job': job_to_update
        }
        return render(request,'updatejob.html', context)

def index(request):
  my_jobs = Jobs.objects.all().values()
  template = loader.get_template('postjobs.html')
  context = {
    'my_jobs': my_jobs,
  }
  return HttpResponse(template.render(context, request))

def addrecord(request):
  job_title_to_save = request.POST.get('job_title')
  job_description_to_save = request.POST.get('job_description')
  new_job = Jobs(job_title=job_title_to_save, job_description=job_description_to_save)
  new_job.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  job_to_delete = Jobs.objects.get(id=id)
  job_to_delete.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request):
    job_id = request.PUT.get('id')
    job_to_update = Jobs.objects.get(id=job_id)

    job_to_update.job_title = request.POST.get('job_title') if request.POST.get('job_title') != None else skip #only update if form has an updated state submitted for job title/description
    job_to_update.job_description = request.POST.get('job_description') if request.POST.get('job_description') != None else skip
    job_to_update.save()
