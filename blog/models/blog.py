"""Model for Blog."""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Review(models.Model):
    """Model for Review."""
    title = models.CharField(max_length=50, blank=False)
    body = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return str(self.title)

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False
