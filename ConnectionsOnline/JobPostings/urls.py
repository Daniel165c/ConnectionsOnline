from django.urls import path
from JobPostings.views import ConnectionsOnlineView


urlpatterns = [
   
    path('', ConnectionsOnlineView.as_view(), name='home'),
]