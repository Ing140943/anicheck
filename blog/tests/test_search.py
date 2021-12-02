from django.forms import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
import blog.models.models_search
import asyncio
import nest_asyncio
from ..forms import CharFieldForm
from django.contrib.auth.models import User

nest_asyncio.apply()

from blog.views.search_view import kitsu_search

import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.decorators import login_required


class QuestionDetailViewTests(TestCase):
    """Objective for test question is question can vote in properly time."""
    def setUp(self):
        super().setUp()
        self.username = "fakeone"
        self.password = "nopassword"
        self.user1 = User.objects.create_user(username=self.username, password=self.password, email="getF@inw007.go.th")
        self.user1.first_name = "Stranger"
        self.user1.save()

    def test_login_view(self):
        """Test that user can login via login view"""
        login_url = reverse("login")
        # Can get to login page
        response = self.client.get(login_url)
        self.assertEqual(200, response.status_code)
        form_data = {"username": "fakeone", "password": "nopassword"}
        response = self.client.post(login_url, form_data)
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, reverse("blog:index"))

