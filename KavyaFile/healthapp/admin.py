from django.contrib import admin
from .models import (
    User, Team, Department, Card, Session, Vote  
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role']  
    search_fields = ['username', 'email']
    list_filter = ['role']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
    search_fields = ['name']
    list_filter = ['department']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'is_active']
    list_filter = ['date', 'is_active']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'team', 'card', 'session', 'vote_value', 'progress']
    list_filter = ['session', 'vote_value']
    search_fields = ['user__username', 'team__name', 'card__title']
