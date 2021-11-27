from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import json


class MyList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mylist = models.TextField(blank=True)

    def set_mylist(self, new_mylist):
        self.mylist = json.dumps(list(new_mylist))

    def get_mylist(self):
        return set(json.loads(self.mylist))

    def add_mylist(self, title):
        title = title.replace('/', '-')
        temp = self.get_mylist()
        temp.add(title)
        self.set_mylist(temp)

    def remove_mylist(self, title):
        title = title.replace('/', '-')
        temp = self.get_mylist()
        temp.remove(title)
        self.set_mylist(temp)

@receiver(post_save, sender=User)
def mylist_create(sender, instance=None, created=False, **kwargs):
    if created:
        MyList.objects.create(user=instance, mylist='[]')
