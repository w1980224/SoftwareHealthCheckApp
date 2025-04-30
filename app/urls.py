from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name='session_list'),
    path('sessions/<int:session_id>/', views.team_list, name='team_list'),
    path('vote/<int:team_id>/<int:session_id>/', views.voting_page, name='voting_page'),
]