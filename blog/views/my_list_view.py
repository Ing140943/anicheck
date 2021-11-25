from django.forms import forms
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import blog.models.models_search
import asyncio
import nest_asyncio
from ..forms import CharFieldForm
nest_asyncio.apply()

my_list = []
def mylist_anime(request):
    return render(request,'blog/mylist.html')

def get_title_to_list(request, anime_title=None):

    if anime_title not in my_list:
        my_list.append(anime_title)
    return render(request, 'blog/mylist.html', context={'anime_title': my_list} )