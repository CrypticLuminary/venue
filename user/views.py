from django.shortcuts import render,redirect

def login_view(request):
    return render(request, 'includes/login.html')

def signin_view(request):
    return render(request,'includes/signup.html')
