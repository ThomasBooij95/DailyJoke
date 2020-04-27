from django.shortcuts import render, redirect
from .models import Joke,Comment,Like, JokeLike
from datetime import datetime, date
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
import stripe
from joke import utils

# strip.api_key = "sk_test_cdUobjjSp9QDZqjGceXHnpzq00dKxZ6Awc"


# Create your views here.
def donate(request): 

    return render(request, 'donate.html')

def charge(request):
    amount =5 
    if request.method =="POST":
        print('Data:', request.POST)
    return redirect(reverse('success', args=[amount]))

def successMsg(request,args):
    amount = args
    context = {'amount':amount}

    return render(request, 'success.html', context)


def home_view(request):
    context = utils.getContext(request)
    return render(request, 'home.html', context)


def like_view(request):
    if request.method=="POST":
        
        currentJoke = utils.getCurrentJoke()
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
    
    currentJoke = utils.getCurrentJoke()
    currentUser = request.user
    if request.method== "POST":
        
        commentText = request.POST.get("Add Comment")
        pic_id = utils.getPicNumberUser(currentUser)
        commentObject = Comment(text = commentText, joke = currentJoke, user = currentUser, pic_id = pic_id)
        commentObject.save()
   
    return redirect("/")
