from django.contrib import admin
from .models import Session, Team, Card, Vote

class SessionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.full_clean()  # This runs model validation (including clean())
        super().save_model(request, obj, form, change)

admin.site.register(Team)
admin.site.register(Card)
admin.site.register(Session,SessionAdmin)
admin.site.register(Vote)

