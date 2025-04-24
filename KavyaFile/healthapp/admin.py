from django.contrib import admin
from .models import CustomUser, Department, Team, Session, Card, Vote
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(Session)
admin.site.register(Card)
admin.site.register(Vote)
