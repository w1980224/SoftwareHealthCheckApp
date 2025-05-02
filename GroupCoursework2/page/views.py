from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile


def begin_health_check(request):
    return redirect('session_list')
    
def view_summary(request):
    return HttpResponse("Summary page (to be implemented)")

def view_progress(request):
    return HttpResponse("Progress page (to be implemented)")

def view_cards(request):
    return HttpResponse("Cards page (to be implemented)")

@login_required
def engineer_landing(request):
    if request.user.profile.role != 'engineer':
        return render(request, 'permission_denied.html')
    return render(request, 'page/engineer.html')

@login_required
def team_leader_landing(request):
    if request.user.profile.role != 'team_leader':
        return render(request, 'permission_denied.html')
    return render(request, 'page/team_leader.html')

@login_required
def department_leader_landing(request):
    if request.user.profile.role != 'department_leader':
        return render(request, 'permission_denied.html')
    return render(request, 'page/department_leader.html')

@login_required
def senior_manager_landing(request):
    if request.user.profile.role != 'senior_manager':
        return render(request, 'permission_denied.html')
    return render(request, 'page/senior_manager.html')