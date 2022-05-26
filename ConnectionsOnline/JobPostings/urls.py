from django.urls import path
from JobPostings.views import *


urlpatterns = [
   
    path('', ConnectionsOnlineView.as_view(), name='home'),
    path('postjobs/', PostJobsViews.as_view(), name='postjobs'),
    #path('add_Joblistings', views.add_joblistings, name ='Joblistings'),
]