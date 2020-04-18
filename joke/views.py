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
        "comments" : comments
        }
    return render(request, 'base.html', context)


def getComments(jokeId):
    allComments = Comment.objects.filter(joke_id = jokeId)
    commentArray  = []

    for comment in allComments:
        commentArray.append(comment.text)

    return commentArray

def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def getJokeNumber():
    today = date.today().strftime("%Y-%m-%d")
    date_begin= '2020-05-10'
    jokeNr = days_between(today,date_begin)%100
    return jokeNr


def like(request):
    if request.method=="POST":
        jokeNumber = getJokeNumber()
        jokes = Joke.objects.all()
        joke = jokes[jokeNumber]
        joke.addLike()
        print("Likes: ", joke.likes)
    else:
        jokeNumber = getJokeNumber()
        joke = jokes[jokeNumber]

    context = {
    "joke" : joke.joke,
    "likes": joke.likes
    }
    return render(request, 'base.html', context)




