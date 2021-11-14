"""Model create form user getting via signup procedure."""
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    """User profile."""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, null=True, blank=False, default="Some")

    

    def __str__(self):
        return str(self.user)
