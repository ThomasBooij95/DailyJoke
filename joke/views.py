from django.shortcuts import render
from .models import Joke
# Create your views here.


def joke_view(request):
    joke = Joke.objects.get(id=1)
    context = {
        "joke" : joke.joke
    }
    return render(request, 'joke_template.html', context)
