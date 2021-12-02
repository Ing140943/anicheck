"""Search function testing for project"""
from django.test import TestCase
import requests
import nest_asyncio
from django.contrib.auth.models import User

nest_asyncio.apply()


def make_dummy_url():
    original = str("http://anicheck-isp.herokuapp.com/kitsu/search?keyword=")
    for i in range(0, 5000):
        original += "f"
    return str(original)


class SearchTests(TestCase):
    """Objective for test is how the result return when searching on deploy website."""

    def setUp(self):
        super().setUp()
        self.username = "fakeone"
        self.password = "nopassword"
        self.user1 = User.objects.create_user(username=self.username, password=self.password, email="getF@inw007.go.th")
        self.user1.first_name = "Stranger"
        self.user1.save()

    def test_search(self):
        """Test that user can search anime normally"""
        urls = requests.get("http://anicheck-isp.herokuapp.com/")
        # Can get to login page
        self.assertEqual(200, urls.status_code)
        response = requests.get("http://anicheck-isp.herokuapp.com/kitsu/Acchi%20Kocchi%20(TV)/")
        self.assertEqual(200, response.status_code)

    def test_blank_search(self):
        """Test that user can search for the blank line that not make crash or any error."""
        urls = requests.get("http://anicheck-isp.herokuapp.com/")
        # Can get to login page
        self.assertEqual(200, urls.status_code)
        response = requests.get("http://anicheck-isp.herokuapp.com/kitsu/search?keyword=")
        self.assertEqual(200, response.status_code)

    def test_too_many_search(self):
        """Test for show that user can not search for over than 4095 letters"""
        response = requests.get(make_dummy_url())
        self.assertEqual(400, response.status_code)
