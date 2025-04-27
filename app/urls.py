from django.urls import path
from . import views

urlpatterns = [
    path('vote/<int:team_id>/<int:session_id>', views.voting_page, name='vote'),
]