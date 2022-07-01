from django.urls import path

from JobPostings import views

urlpatterns = [
    path('', views.ConnectionsOnlineView.as_view(), name='home'),
    path('postjobs/create_post', views.addrecord, name='add_job'),
    path('postjobs/', views.index, name='index'),
    path('postjobs/delete/<int:id>', views.delete, name='delete_job'),
    path('postjobs/update', views.update, name='confirm_update'),
    path('postjobs/edit/<int:id>', views.ConnectionsOnlineUpdateView.as_view(), name="update_job")
]