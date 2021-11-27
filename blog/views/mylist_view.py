from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from blog.models.mylist import MyList
from django.contrib.auth.models import User

class MyListView(ListView):
    model = User
    template_name = 'blog/mylist.html'

    def get_context_data(self, *args, **kwargs):
        locate = get_object_or_404(User, id=self.kwargs['pk'])
        object_list = locate.mylist.get_mylist()

        context = super(MyListView, self).get_context_data(locate=locate, object_list=object_list, **kwargs)
        return context

# def mylist(request):
#     return render(request, 'blog/mylist.html')