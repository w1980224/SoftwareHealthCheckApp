from django.contrib.auth.models import User
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

class Profile(models.Model):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_leader', 'Team Leader'),
        ('department_leader', 'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username