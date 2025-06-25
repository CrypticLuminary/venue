from django.shortcuts import render,HttpResponse
from django.views.generic import DetailView
from .models import Home

class homeDetail(DetailView):
    model = Home
    template_name = 'base.html'

    def get_object(self, queryset = None):
        return Home.objects.first()

   
    

