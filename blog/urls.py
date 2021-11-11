"""This module use for specify the path of the web application."""

from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:num>/', views.about),
    path('kitsu/<str:title>/', views.kitsu, name='kitsu'),
    path('kitsu/search', views.kitsu_search, name='search'),
    path('charfield/', views.charfield),
]
