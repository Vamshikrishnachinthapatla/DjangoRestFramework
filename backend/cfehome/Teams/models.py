from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Team(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=120)
    sponsor = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    trophies = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name