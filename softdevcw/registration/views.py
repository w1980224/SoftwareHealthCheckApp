from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        confirmedpassword = request.POST['confirmedpassword']

        if password == confirmedpassword:
            user = User.objects.create_user(username=username, password=password, email=email, role=role)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"the passwords do not match, please try again")

    return render(request, "registration/signup.html")

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
        
    return render(request,'registration/login.html')

def logout(request):
    logout(request)
    return redirect ('login')


    