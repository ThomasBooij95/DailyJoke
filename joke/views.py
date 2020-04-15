from django.shortcuts import render
from .models import Joke
from datetime import datetime, date
# Create your views here.


def joke_view(request):
    jokeId = getJokeId()
    allJokes = Joke.objects.all()
    joke = allJokes[jokeId]
    context = {
        "joke" : joke.joke,
        "likes": joke.likes
    }
    return render(request, 'base.html', context)




def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def getJokeId():
    today = date.today().strftime("%Y-%m-%d")
    date_begin= '2020-04-10'
    jokeNr = days_between(today,date_begin)%100
    return jokeNr

def like(request):
    if request.method=="POST":
        jokeID = getJokeId()
        jokes = Joke.objects.all()
        joke = jokes[jokeID]
        joke.addLike()
        print("Likes: ", joke.likes)
    else:
        jokeID = getJokeId()
        joke = jokes[jokeID]

    context = {
    "joke" : joke.joke,
    "likes": joke.likes
    }
    return render(request, 'base.html', context)




