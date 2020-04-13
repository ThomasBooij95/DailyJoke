from django.shortcuts import render
from .models import Joke
from datetime import datetime, date
# Create your views here.


def joke_view(request):
    jokeId = getJokeId()
    allJokes = Joke.objects.all()
    joke = allJokes[jokeId]
    context = {
        "joke" : joke.joke
    }
    return render(request, 'base.html', context)




def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def getJokeId():
    today = date.today().strftime("%Y-%m-%d")
    date_begin= '2020-04-11'
    jokeNr = days_between(today,date_begin)%100
    return jokeNr


