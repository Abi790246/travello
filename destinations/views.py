from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models  import auth,User
# Create your views here.
def mumbai(request):
    return render(request,'index1.html')
def hyderbad(request):
    return redirect('/')
def bengaluru(request):
    return redirect('/')
def delhi(request):
    return redirect('/')
