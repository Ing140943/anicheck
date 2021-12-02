"""Deployment test for project """
from django.test import TestCase
import requests


class DeploymentTests(TestCase):
    """Objective for test deployment on heroku hosting"""

    def test_web_deploy(self):
        """Test for deployment on heroku"""
        heroku_web = requests.get('http://anicheck-isp.herokuapp.com/')
        self.assertEqual(heroku_web.status_code, 200)
