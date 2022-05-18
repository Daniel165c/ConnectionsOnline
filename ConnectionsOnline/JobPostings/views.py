from django.shortcuts import render
from django.views import View

# from paintapp.forms import ColorPickerForm

# Create your views here.

class ConnectionsOnlineView(View):
    def get(self, request):
        return render(request=request, template_name='home.html')

class PostJobsViews(View):
    def get(self, request):
        return render(request=request,
        template_name='postjobs.html')