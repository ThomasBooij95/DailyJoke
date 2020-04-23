from django.shortcuts import render, redirect
from .models import Joke,Comment,Like, JokeLike
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your views here.

def getContext(request):

    current_user = request.user
    current_joke = getCurrentJoke()

    #Check if user liked the joke, gives boolean 
    likedJoke = JokeLike.userLikedJoke(current_user = current_user, current_joke = current_joke)
    comments = getComments(current_joke.id)

    likes = countJokeLikes(current_joke)
    # likedJoke = 
    context = {
        "joke" : current_joke.joke,
        "likes": likes,
        "comments" : comments,
        "likedJoke": likedJoke,
        }
    return context

def home_view(request):
    context = getContext(request)
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
    date_begin= '2020-05-11'
    jokeNr = days_between(today,date_begin)%100
    return jokeNr

def getCurrentJoke():
    jokeNumber = getJokeNumber()
    jokes = Joke.objects.all()
    current_joke = jokes[jokeNumber]
    return current_joke

def countJokeLikes(joke):

    #Counts number of times joke is in the JokeLike list
    jokeEntries = JokeLike.objects.filter(joke = joke)
    likes = jokeEntries.count()
    return likes


def like_view(request):
    if request.method=="POST":
        
        current_user = request.user
        current_joke = getCurrentJoke()

        #Check if user liked the joke: True if liked, False if not liked
        likedJoke = JokeLike.userLikedJoke(current_user = current_user, current_joke = current_joke)

        if not likedJoke:
            #Add the like to the JokeLike table
            jokeLike = JokeLike(user = current_user, joke = current_joke)
            jokeLike.save()       
        else:
            print("Already liked this joke!")

    context = getContext(request)
    return redirect('home')


def comment_view(request):
    
    currentJoke = getCurrentJoke()

    if request.method== "POST":
        commentText = request.POST.get("Add Comment")
        print('Commented text: ',commentText)
        commentObject = Comment(text = commentText, joke = currentJoke)
        commentObject.save()
   
    return redirect("/")

def parse_refer(url):
    split = url.split('/')
    return split[-1]


