import nest_asyncio
from django.contrib.auth.models import User

nest_asyncio.apply()


from django.test import TestCase, Client
import requests

def make_dummy_url():
    original = str("http://anicheck-isp.herokuapp.com/kitsu/search?keyword=")
    for i in range(0,5000):
        original += "f"
    return str(original)


class QuestionDetailViewTests(TestCase):
    """Objective for test question is question can vote in properly time."""

    def setUp(self):
        super().setUp()
        self.username = "fakeone"
        self.password = "nopassword"
        self.user1 = User.objects.create_user(username=self.username, password=self.password, email="getF@inw007.go.th")
        self.user1.first_name = "Stranger"
        self.user1.save()

    def test_search(self):
        """Test that user can login via login view"""
        urls = requests.get("http://anicheck-isp.herokuapp.com/")
        # Can get to login page
        self.assertEqual(200, urls.status_code)
        response = requests.get("http://anicheck-isp.herokuapp.com/kitsu/Acchi%20Kocchi%20(TV)/")
        self.assertEqual(200, response.status_code)

    def test_blank_search(self):
        urls = requests.get("http://anicheck-isp.herokuapp.com/")
        # Can get to login page
        self.assertEqual(200, urls.status_code)
        response = requests.get("http://anicheck-isp.herokuapp.com/kitsu/search?keyword=")
        self.assertEqual(200, response.status_code)

    def test_too_many_search(self):
        response = requests.get(make_dummy_url())
        self.assertEqual(400, response.status_code)

