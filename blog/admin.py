from django.contrib import admin
from blog.models.blog import Review
from blog.models.anime import Anime

# Register your models here.
admin.site.register(Review)
admin.site.register(Anime)
