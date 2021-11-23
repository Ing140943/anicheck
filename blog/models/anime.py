from django.db import models
from django.contrib.auth.models import User


class Anime(models.Model):
    title = models.CharField(blank=False)
    url = models.CharField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
