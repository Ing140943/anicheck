from django.shortcuts import render
from django.http import HttpResponse
import blog.models
import asyncio
import nest_asyncio
nest_asyncio.apply()
# from blog.models import *
# Create your views here.

def index(request):
    return render(request, 'blog/blog_index.html', )


def about(request, num):
    return HttpResponse(f"This is a test of Django framework number: {num}")

async def kitsu(request, title):
    if title == None:
        return HttpResponse("กรอกด้วยไอสัส")
    loop = asyncio.get_event_loop()
    loop.create_task(blog.models.anime_search(title))
    # print(blog.models.api_uses(title))
    data = loop.run_until_complete(asyncio.gather(blog.models.anime_search(title)))
    return HttpResponse(data)

def test_kit():
    return blog.models.api_uses('naruto')

def about(request):
    return HttpResponse("This is a test of Django framework")


def result_demo(request):
    return render(request, 'blog/show_detail.html', )
