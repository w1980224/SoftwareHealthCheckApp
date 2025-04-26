from django.db import models

class Vote(models.Model):
    option_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def _str__(self):
        return self.option_name