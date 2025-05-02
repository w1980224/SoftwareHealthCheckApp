from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile


def begin_health_check(request):
    return HttpResponse("Begin Health Check page (to be implemented)")

def view_summary(request):
    return HttpResponse("Summary page (to be implemented)")

def view_progress(request):
    return HttpResponse("Progress page (to be implemented)")

def view_cards(request):
    return HttpResponse("Cards page (to be implemented)")


def engineer_landing(request):
    return render(request, 'page/engineer.html')

def team_leader_landing(request):
    return render(request, 'page/team_leader.html')

def department_leader_landing(request):
    return render(request, 'page/department_leader.html')

def senior_manager_landing(request):
    return render(request, 'page/senior_manager.html')
    