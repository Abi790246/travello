from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models  import auth,User

# Create your views here.
def register(request):
    if(request.method=='POST'):
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                 user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password1,email=email)
                 user.save()
                 return render(request,'login.html')
                 print('user created')
        else:
            return redirect('register')
        return redirect('/')

    return render (request,'register.html')
def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Invalid credentials')
                return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')