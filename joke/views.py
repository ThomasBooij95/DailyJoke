from django.shortcuts import render, redirect
from .models import Joke,Comment
from datetime import datetime, date
# Create your views here.

def getContext():
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
    return context

def home_view(request):
    context = getContext()
    return render(request, 'home.html', context)


def getComments(jokeId):
    allComments = Comment.objects.filter(joke_id = jokeId)
    commentArray  = []

    for comment in allComments:
        commentArray.append(comment)

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


def like_view(request):
    if request.method=="POST":
        jokeNumber = getJokeNumber()
        jokes = Joke.objects.all()
        joke = jokes[jokeNumber]
        joke.addLike()
        print("Likes: ", joke.likes)
    else:
        jokeNumber = getJokeNumber()
        jokes = Joke.objects.all()
        joke = jokes[jokeNumber]

    context = getContext()
    return render(request, 'liked.html', context)


def comment_view(request):
    if request.method== "POST":
        commentText = request.POST.get("Add Comment")
        print(commentText)

        jokeNumber = getJokeNumber()
        jokes = Joke.objects.all()
        currentJoke = jokes[jokeNumber]

        commentObject = Comment(text = commentText, joke = currentJoke)
        commentObject.save()

        

    else:
        jokeNumber = getJokeNumber()
        jokes = Joke.objects.all()
        joke = jokes[jokeNumber]

    context = getContext()

    url = request.META.get("HTTP_REFERER")
    refer = parse_refer(url)

    if refer == '':
        return redirect("/")
    elif refer == 'liked':
        return redirect('/liked')
    else:
        return redirect("/")

def parse_refer(url):
    split = url.split('/')
    return split[-1]


