from django.urls import path
from . import views

urlpatterns = [
   
    path('begin_health_check/', views.begin_health_check, name='begin_health_check'),
    path('view_summary/', views.view_summary, name='view_summary'),
    path('view_progress/', views.view_progress, name='view_progress'),
    path('view_cards/', views.view_cards, name='view_cards'),

    # Optional direct access
    path('engineer/', views.engineer_landing, name='engineer'),
    path('team_leader/', views.team_leader_landing, name='team_leader'),
    path('department_leader/', views.department_leader_landing, name='department_leader'),
    path('senior_manager/', views.senior_manager_landing, name='senior_manager'),
]