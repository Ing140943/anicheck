from django.forms import forms
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import blog.models.models_search
import asyncio
import nest_asyncio
from ..forms import CharFieldForm
nest_asyncio.apply()


def mylist_anime(request):
    return render(request,'blog/mylist.html')

# async def get_title_to_list(request, anime_title):
#     keyword = request.GET[anime_title]
#     loop = asyncio.get_event_loop()
#     loop.create_task(blog.models.models_search.anime_search_title(keyword))
#     data = loop.run_until_complete(asyncio.gather(blog.models.models_search.anime_search_title(keyword)))[0]
#     return render(request, 'blog/show_detail.html', context={'anime_title': data