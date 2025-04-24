from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_leader', 'Team Leader'),
        ('department_leader', 'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

class Session(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return f"{self.title} - {self.date}"

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Vote(models.Model):
    TRAFFIC_LIGHT_CHOICES = [
        ('green', 'Green'),
        ('amber', 'Amber'),
        ('red', 'Red'),
    ]
    TREND_CHOICES = [
        ('up', 'Getting Better'),
        ('same', 'No Change'),
        ('down', 'Getting Worse'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    vote = models.CharField(max_length=10, choices=TRAFFIC_LIGHT_CHOICES)
    trend = models.CharField(max_length=10, choices=TREND_CHOICES)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.card.title} ({self.vote})"
