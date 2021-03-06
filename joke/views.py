from django.shortcuts import render, redirect
from .models import Joke,Comment,Like, JokeLike
from datetime import datetime, date
from django.contrib.auth.models import User
# Create your views here.

def getPicNumberUser(user):
    
    picnumber = str(user.id%8)
    if user.is_superuser:
        picnumber = "admin"
    return picnumber

def getContext(request):

    currentUser = request.user
    currentJoke = getCurrentJoke()



    if currentUser.is_anonymous:
        profile_pic = "joke/img/anonymous_dad.jpeg"
    else:
        picnumber = getPicNumberUser(currentUser)
        profile_pic = "joke/img/"+picnumber+".jpeg"


    #Check if user liked the joke, gives boolean 
    likedJoke = JokeLike.userLikedJoke(current_user = currentUser, current_joke = currentJoke)
    comments = getComments(currentJoke.id)
    
    likes = countJokeLikes(currentJoke)
    # Check whether the Joke has an author and give its username to context.
    if(currentJoke.author):
        authorJoke = currentJoke.author.username
    else:
        authorJoke = ''
    

    # likedJoke = 
    context = {
        "joke" : currentJoke.joke,
        "likes": likes,
        "comments" : comments,
        "likedJoke": likedJoke,
        "profile_pic": profile_pic,
        "author": authorJoke
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
    date_begin= '2020-04-10'
    jokeNr = days_between(today,date_begin)%100
    return jokeNr

def getCurrentJoke():

    jokeNumber = getJokeNumber()
    jokes = Joke.objects.all().filter(override=True)
    print(jokes)
    if not jokes: # When no jokes are featured with the admin
        jokes = Joke.objects.all()
        current_joke = jokes[jokeNumber]
    else:
        current_joke = jokes[0]
    return current_joke

def countJokeLikes(joke):

    #Counts number of times joke is in the JokeLike list
    jokeEntries = JokeLike.objects.filter(joke = joke)
    likes = jokeEntries.count()
    return likes


def like_view(request):
    if request.method=="POST":
        
        currentJoke = getCurrentJoke()
        currentUser = request.user

        #Check if user liked the joke: True if liked, False if not liked
        likedJoke = JokeLike.userLikedJoke(current_user = currentUser, current_joke = currentJoke)

        if not likedJoke:
            #Add the like to the JokeLike table
            jokeLike = JokeLike(user = currentUser, joke = currentJoke)
            jokeLike.save()       
        else:
            print("Already liked this joke!")

    return redirect('home')


def comment_view(request):
    
    currentJoke = getCurrentJoke()
    currentUser = request.user
    if request.method== "POST":
        
        commentText = request.POST.get("Add Comment")
        pic_id = getPicNumberUser(currentUser)
        commentObject = Comment(text = commentText, joke = currentJoke, user = currentUser, pic_id = pic_id)
        commentObject.save()
   
    return redirect("/")

def parse_refer(url):
    split = url.split('/')
    return split[-1]


