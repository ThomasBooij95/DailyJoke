from django.shortcuts import render, redirect
from .models import Joke,Comment,Like, JokeLike
from datetime import datetime, date
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse

from joke import utils

import time
from mollie.api.client import Client
from mollie.api.error import Error




# Create your views here.
def donate(request): 

    api_key = "test_bsjDvHFFe97grVyf9rnWpQnJd8p9P4"
    mollie_client = Client()
    mollie_client.set_api_key(api_key)

    if request.method == "POST":
        issuer_id = request.POST.get("issuer")    
        # Generate a unique webshop order id for this example. It is important to include this unique attribute
        # in the redirectUrl (below) so a proper return page can be shown to the customer.
        #
        my_webshop_id = int(time.time())
        payment = mollie_client.payments.create({
            'amount': {
                'currency': 'EUR',
                'value': '10.00'
            },
            'description': 'My first API payment',
            'webhookUrl': 'https://google.com',
            'redirectUrl': 'http://google.com',
            'metadata': {
                'my_webshop_id': str(my_webshop_id),
            },
            'method': 'ideal',
            'issuer': issuer_id,
        })
        return redirect(payment.checkout_url)


    issuers =  mollie_client.methods.get('ideal', include='issuers').issuers
    context = {"issuers" : issuers}



    return render(request, 'donate.html', context)

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
