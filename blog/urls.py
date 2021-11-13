"""This module use for specify the path of the web application."""

from django.urls import path

import blog.views.search_view
import blog.views.review_view

app_name = 'blog'

urlpatterns = [
    path('', blog.views.search_view.index, name='index'),
    path('kitsu/<str:title>/', blog.views.search_view.kitsu, name='kitsu'),
    path('kitsu/search', blog.views.search_view.kitsu_search, name='search'),
    path('reviews/', blog.views.review_view.ReviewsView.as_view(), name='reviews'),
    path('create-review/', blog.views.review_view.CreateReviewView.as_view(success_url="/reviews"), name='create-review'),
]
