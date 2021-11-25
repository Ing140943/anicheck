from django.db import models
from django.contrib.auth.models import User


class Anime(models.Model):
    title = models.TextField(blank=False)
    url = models.TextField(blank=False),
    user = models.ForeignKey(User, on_delete=models.CASCADE)
