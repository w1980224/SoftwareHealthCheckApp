from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    team_leaders = models.ManyToManyField(User, related_name='team_leaders')

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Vote(models.Model):
    VOTE_CHOICES = [
        (1, 'Red'),
        (2, 'Yellow'),
        (3, 'Green'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_CHOICES)
    session = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return f"{self.user.username} - {self.card.name} - {self.vote}"

class Session(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def _str__(self):
        return f"Session {self.id} for {self.team.name}"
