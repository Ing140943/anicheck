"""This module use for specify the path of the web application."""

from django.urls import path

import blog.views.search_view
import blog.views.review_view
import blog.views.about_us_view
import blog.views.user_view
import blog.views.mylist_view

app_name = 'blog'

urlpatterns = [

    path('', blog.views.search_view.index, name='index'),
    path('kitsu/<str:title>/', blog.views.search_view.kitsu, name='kitsu'),
    path('kitsu/search', blog.views.search_view.kitsu_search, name='search'),
    path('reviews/', blog.views.review_view.ReviewsView.as_view(), name='reviews'),
    path('create-review/', blog.views.review_view.CreateReviewView.as_view(success_url="/reviews"), name='create-review'),
    path('contact/', blog.views.about_us_view.about_us, name='contact'),
    path('profile/<int:pk>', blog.views.user_view.ProfilePageView.as_view(), name='profile'),
    path('profile/edit', blog.views.user_view.update_user, name='profile-edit'),
    path('profile/<int:pk>/mylist/', blog.views.mylist_view.MyListView.as_view(), name='mylist'),
    path('profile/<int:pk>/mylist/add/<str:title>', blog.views.search_view.add_mylist, name='add-mylist'),
    path('profile/<int:pk>/mylist/remove/<str:title>', blog.views.search_view.remove_mylist, name='remove-mylist'),
]
