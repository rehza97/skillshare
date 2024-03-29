import django_filters

from job.models import *

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['title','category','Wilaya',]
        