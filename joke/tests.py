from django.test import TestCase
from .models import Joke
# Create your tests here.
class JokeTestCase(TestCase):
    def setUp(self):
        Joke.objects.create(joke="Testjoke1")
        print("running setup..")
    def test_joke(self):
        joke1 = Joke.objects.get(joke="Testjoke1")
        self.assertEqual(joke1.joke,"Testjoke1")
