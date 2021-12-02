from django.test import TestCase, Client
import requests


class QuestionDetailViewTests(TestCase):
    """Objective for test question is question can vote in properly time."""

    def test_web_deploy(self):
        heroku_web = requests.get('http://anicheck-isp.herokuapp.com/')
        self.assertEqual(heroku_web.status_code, 200)

