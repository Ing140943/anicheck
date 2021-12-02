from django.test import TestCase
import requests


class DeploymentTests(TestCase):
    """Objective for test deploy ment on heroku hosting"""
    def test_web_deploy(self):
        heroku_web = requests.get('http://anicheck-isp.herokuapp.com/')
        self.assertEqual(heroku_web.status_code, 200)

