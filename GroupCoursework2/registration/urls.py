from django.urls import path
from .views import home, signup, login_view, logout_view

app_name = 'registration'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]