from django.forms import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
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
    return render(request, 'blog/show_detail.html', context={
        "url": title,
        "title": data[next(iter(data))]['names'],
        "sub_type": data[next(iter(data))]['sub-type'],
        "status": data[next(iter(data))]['status'],
        "synopsis": data[next(iter(data))]['synopsis'],
        "episode": data[next(iter(data))]['episode'],
        "age_rating": data[next(iter(data))]['age-rating'],
        "popularity": data[next(iter(data))]['popularity'],
        "rating": data[next(iter(data))]['rating'],
        "image" : data[next(iter(data))]['images'],
    })


async def kitsu_search(request):
    keyword = request.GET['keyword']
    loop = asyncio.get_event_loop()
    loop.create_task(blog.models.models_search.anime_search_title(keyword))
    # print(blog.models.api_uses(title))
    data = loop.run_until_complete(asyncio.gather(blog.models.models_search.anime_search_title(keyword)))[0]
    print(data)
    return render(request, 'blog/search.html', context={'title_list': data})


def charfield(request):
    if request.method == 'POST':
        forms = CharFieldForm(request.POST)
    else:
        form = CharFieldForm()
    return render(request, 'blog/charfield.html', {'form': 'form'})

def review_anime(request):
    return render(request, 'blog/review.html')

@login_required
def add_mylist(request, title, pk):
    print(title)
    request.user.mylist.add_mylist(title)
    request.user.mylist.save()
    return redirect('blog:mylist', pk=pk)


@login_required
def remove_mylist(request, title, pk):
    request.user.mylist.remove_mylist(title)
    request.user.mylist.save()
    return redirect('blog:mylist', pk=pk)
