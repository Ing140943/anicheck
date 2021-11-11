"""Model for Blog."""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone




class BlogForum(models.Model):
    """Model for Forum."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Model for Blog."""
    title = models.CharField(max_length=50)
    short_description = models.TextField(blank=True)
    body = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes', blank=True)
    forum = models.ForeignKey(BlogForum, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return str(self.title)

    def like_amount(self):
        return self.likes.count()

    def dislike_amount(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('kuhub:blog-detail', kwargs={'pk': self.pk})

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False


class BlogReport(models.Model):
    """Model for report."""
    TOPIC_CHOICES = (
        ('Fake news', 'Fake news'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'),
        ('Threat', 'Threat'), ('Violence', 'Violence'), ('Indecent words', 'Indecent words'),
        ('Sexual Content', 'Sexual Content'), ('Others', 'Others')
    )

    blog = models.ForeignKey(Blog, related_name="reports", on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[Blog: %s] Topic: "%s" reported by %s, %s' \
               % (self.blog, self.topic, self.author, self.pub_date)