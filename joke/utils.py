from datetime import datetime, date
from .models import Joke,Comment,Like, JokeLike


def getComments(jokeId):
    allComments = Comment.objects.filter(joke_id = jokeId)
    commentArray  = []

    for comment in allComments:
        commentArray.append(comment)

    return commentArray

def parse_refer(url):
    split = url.split('/')
    return split[-1]



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


def getPicNumberUser(user):
    
    picnumber = str(user.id%8)
    if user.is_superuser:
        picnumber = "admin"
    return picnumber


def getContext(request):

    currentUser = request.user
    currentJoke = getCurrentJoke()


    if currentUser.is_anonymous:
        profile_pic = "img/anonymous_dad.jpeg"
    else:
        picnumber = getPicNumberUser(currentUser)
        profile_pic = "img/"+picnumber+".jpeg"


    #Check if user liked the joke, gives boolean 
    likedJoke = JokeLike.userLikedJoke(current_user = currentUser, current_joke = currentJoke)
    comments = getComments(currentJoke.id)

    likes = countJokeLikes(currentJoke)
    # likedJoke = 
    context = {
        "joke" : currentJoke.joke,
        "likes": likes,
        "comments" : comments,
        "likedJoke": likedJoke,
        "profile_pic": profile_pic,

        }
    return context
