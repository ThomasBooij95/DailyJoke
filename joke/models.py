from django.db import models
from django.urls import reverse

# Create your models here.


class Joke(models.Model):
    joke = models.TextField()
    likes = models.IntegerField(default=0)
    # description = models.TextField(blank=True, null=True)
    
    def addLike(self):
        self.likes = self.likes + 1
        self.save()
    def addJoke(self, jokeText):
        self.joke = jokeText
        self.save()



       
class Comment(models.Model):
    joke = models.ForeignKey(Joke,on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)    
    author = models.TextField(default = "Anonymous Dad")
    
    def addLike(self):
        self.likes = self.likes + 1
        self.save()
