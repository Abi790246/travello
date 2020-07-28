from django.shortcuts import render,redirect
from .models import destination
from django.db.models import Q
from django.contrib.auth.models  import auth,User
def index(request):
    dests=destination.objects.all()
    return render(request,"index.html",{'dests':dests})
def search(request):
    query = request.POST['desti']
    object_list = destination.objects.filter(Q(name__icontains=query))
    return render(request,"search.html",{'object_list':object_list})
def logout(request):
    auth.logout(request)
    return redirect('/')
        



    