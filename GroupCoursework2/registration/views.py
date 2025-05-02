from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from page.models import Profile

@login_required
def home(request):
    role = request.user.profile.role
    if role == 'engineer':
        return redirect('engineer')
    elif role == 'team_leader':
        return redirect('team_leader')
    elif role == 'department_leader':
        return redirect('department_leader')
    elif role == 'senior_manager':
        return redirect('senior_manager')
    else:
        return redirect('login')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        confirmedpassword = request.POST['confirmedpassword']

        if password == confirmedpassword:
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.create(user=user, role=role)
            auth_login(request, user)

            if role == "engineer":
                return redirect('engineer')
            elif role == "team_leader":
                return redirect('team_leader')
            elif role == "department_leader":
                return redirect('department_leader')
            elif role == "senior_manager":
                return redirect('senior_manager')
            else:
                return redirect('home')
        else:
            messages.error(request, "The passwords do not match. Please try again.")

    return render(request, "registration/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            try:
                profile = Profile.objects.get(user=user)
                role = profile.role
                if role == "engineer":
                    return redirect('engineer')  
                elif role == "team_leader":
                    return redirect('team_leader')
                elif role == "department_leader":
                    return redirect('department_leader')
                elif role == "senior_manager":
                    return redirect('senior_manager')
                else:
                    return redirect('home')  
            except Profile.DoesNotExist:
                messages.error(request, "User profile not found.")
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')