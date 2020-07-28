from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,"contact.html")
def news(request):
    return render(request,"news.html")
def about(request):
    return(request,"about.html")