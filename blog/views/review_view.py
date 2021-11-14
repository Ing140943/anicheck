from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from blog.models.blog import Review

class ReviewsView(ListView):
    model = Review
    template_name = 'blog/reviews.html'
    ordering = ['-pub_date']
    context_object_name = 'reviews'
    paginate_by = 10

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'blog/create_review.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False
