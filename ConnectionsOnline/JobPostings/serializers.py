from rest_framework import serializers
from JobPostings.models import Jobs

class JobPostingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"