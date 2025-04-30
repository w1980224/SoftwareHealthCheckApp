from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile

# Main landing page

#def landing(request):

   # if request.user.is_authenticated:
        #try:
           # profile = Profile.objects.get(user=request.user)
           # if profile.role == 'engineer':
            #    return render(request, 'page/engineer.html', {'profile': profile})
           # elif profile.role == 'team_leader':
            #    return render(request, 'page/team_leader.html', {'profile': profile})
           # elif profile.role == 'department_leader':
            #    return render(request, 'page/department_leader.html', {'profile': profile})
           # elif profile.role == 'senior_manager':
            #    return render(request, 'page/senior_manager.html', {'profile': profile})
       
    # except Profile.DoesNotExist:
         #   return render(request, "page/landing.html")  # fallback page
   # else:
       # return render(request, "page/landing.html")

# Stub views for feature pages
def begin_health_check(request):
    return HttpResponse("Begin Health Check page (to be implemented)")

def view_summary(request):
    return HttpResponse("Summary page (to be implemented)")

def view_progress(request):
    return HttpResponse("Progress page (to be implemented)")

def view_cards(request):
    return HttpResponse("Cards page (to be implemented)")

# Role-specific pages (if needed separately from `landing`)
def engineer_landing(request):
    return render(request, 'page/engineer.html')

def team_leader_landing(request):
    return render(request, 'page/team_leader.html')

def department_leader_landing(request):
    return render(request, 'page/department_leader.html')

def senior_manager_landing(request):
    return render(request, 'page/senior_manager.html')
    