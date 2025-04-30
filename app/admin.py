from django.contrib import admin
from .models import Session, Team, Card, Vote

admin.site.register(Team, TeamAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Vote, VoteAdmin)

