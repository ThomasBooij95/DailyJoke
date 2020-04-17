from django.shortcuts import render
from .models import Joke,Comment
from datetime import datetime, date
# Create your views here.


def joke_view(request):
    jokeNumber = getJokeNumber()
    allJokes = Joke.objects.all()
    joke = allJokes[jokeNumber]
    jokeId = joke.id
    comments = getComments(jokeId)
    context = {
        "joke" : joke.joke,
        "likes": joke.likes,
        "commentText" : comments[0].text
    }
    return render(request, 'base.html', context)


def getComments(jokeId):
    allComments = Comment.objects.filter(joke_id = jokeId)
    print(jokeId)
    print(allComments)
    return allComments

def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def getJokeNumber():
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




