from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('Hello,welcome to our website')
    

