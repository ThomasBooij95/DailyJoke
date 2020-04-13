from django.shortcuts import render
from .models import Joke
# Create your views here.


def joke_view(request):
    joke = Joke.objects.get(id=3)
    context = {
        "joke" : joke.joke
    }
    return render(request, 'base.html', context)
