from django.urls import path
from . import views

urlpatterns = [
    path('', views.voting_page, name='vote'),
]