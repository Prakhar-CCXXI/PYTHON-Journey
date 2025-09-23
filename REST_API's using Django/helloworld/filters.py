import django_filters
from ansible_collections.community.dns.plugins.modules.wait_for_txt import lookup
from django import forms

from helloworld.models import Post



class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}) , lookup_expr = "date__exact" )


    class Meta:
        model = Post
        fields = ['created_on',]