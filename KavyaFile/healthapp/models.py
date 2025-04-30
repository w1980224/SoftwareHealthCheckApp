from django.db import models
from django.contrib.auth.models import AbstractUser

# Extending the default user model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_lead', 'Team Leader'),
        ('dept_lead', 'Department Leader'),
        ('senior_mgr', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.department.name}"

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Session(models.Model):
    date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Session on {self.date}"

class Vote(models.Model):
    VOTE_CHOICES = [
        ('green', 'Green'),
        ('amber', 'Amber'),
        ('red', 'Red'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    vote_value = models.CharField(max_length=10, choices=VOTE_CHOICES)
    progress = models.BooleanField(default=False)  # True = improving, False = not

    class Meta:
        unique_together = ('user', 'card', 'session')

    def __str__(self):
        return f"{self.user.username} - {self.card.title} - {self.vote_value}"
