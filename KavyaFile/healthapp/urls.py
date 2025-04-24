from django.urls import path
from .views import summary_view

urlpatterns = [
    path('summary/', summary_view, name='summary'),
]
