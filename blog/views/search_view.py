from django.forms import forms
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import blog.models.models_search
import asyncio
import nest_asyncio
from ..forms import CharFieldForm
nest_asyncio.apply()


def index(request):
    return render(request, 'blog/blog_index.html', )


async def kitsu(request, title):
    if title is None:
        return HttpResponse("กรอกด้วยไอสัส")
    loop = asyncio.get_event_loop()
    loop.create_task(blog.models.models_search.anime_search(title))
    # print(blog.models.api_uses(title))
    data = loop.run_until_complete(asyncio.gather(blog.models.models_search.anime_search(title)))[0]
    print(data)
    return render(request, 'blog/show_detail.html', context={
        "sub_type": data[next(iter(data))]['sub-type'],
        "status": data[next(iter(data))]['status'],
        "synopsis": data[next(iter(data))]['synopsis'],
        "episode": data[next(iter(data))]['episode'],
        "age_rating": data[next(iter(data))]['age-rating'],
        "popularity": data[next(iter(data))]['popularity'],
        "rating": data[next(iter(data))]['rating'],
    })


async def kitsu_search(request):
    keyword = request.GET['keyword']
    loop = asyncio.get_event_loop()
    loop.create_task(blog.models.models_search.anime_search_title(keyword))
    # print(blog.models.api_uses(title))
    data = loop.run_until_complete(asyncio.gather(blog.models.models_search.anime_search_title(keyword)))[0]
    return render(request, 'blog/search.html', context={'title_list': data})


def charfield(request):
    if request.method == 'POST':
        forms = CharFieldForm(request.POST)
    else:
        form = CharFieldForm()
    return render(request, 'blog/charfield.html', {'form': 'form'})

def review_anime(request):
    return render(request, 'blog/review.html')

def mylist_anime(request):
    return render(request,'blog/mylist.html')
