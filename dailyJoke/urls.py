"""dailyJoke URL Configur
        jokeNumber = getJokeNumber(ation

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from joke import views
from register.views import register_view, login_view
# from django.contrib.auth import views as auth_views


urlpatterns = [
    #Joke app
    path('', views.home_view, name='home'),
    path('liked', views.like_view, name = "liked"),
    path('comment', views.comment_view, name ='comment'),
    path('donate', views.donate, name='donate'),
    path('charge', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name='success' ),
    
    #Register app
    path('register', register_view, name ='register'),
    path('login', login_view, name='login'),

    #Django
    path('', include("django.contrib.auth.urls")),
    path('admin', admin.site.urls, name = 'admin'),

]
