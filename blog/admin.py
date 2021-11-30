from django.contrib import admin
from blog.models.blog import Review
from blog.models.mylist import MyList

# Register your models here.
admin.site.register(Review)
admin.site.register(MyList)
