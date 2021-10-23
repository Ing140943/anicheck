"""This module use for specify the path of the web application."""

from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index),
]
