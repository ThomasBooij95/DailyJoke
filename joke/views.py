from django.shortcuts import render
from .models import Joke
from datetime import datetime, date
# Create your views here.


def joke_view(request):
    joke = Joke.objects.get(id=3)
    context = {
        "joke" : joke.joke
    }
    return render(request, 'base.html', context)

