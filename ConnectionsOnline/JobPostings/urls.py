from django.urls import path
from JobPostings.views import *


urlpatterns = [
   
    path('', ConnectionsOnlineView.as_view(), name='home'),
    path('postjobs/', PostJobsView.as_view(), name='postjobs'),
    path('joblist', JobListingsView.as_view(), name ='joblist'),
]