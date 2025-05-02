from django.contrib import admin
from .models import Session, Team, Card, Vote

admin.site.register(Team)
admin.site.register(Card)
admin.site.register(Session)
admin.site.register(Vote)

