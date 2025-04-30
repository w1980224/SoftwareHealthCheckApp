from django.urls import path
from .views import summary_view

urlpatterns = [
    path('', summary_view, name='summary'),  # handles /summary/
]
