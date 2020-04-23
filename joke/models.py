from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    author = models.TextField(default = "Anonymous Dad")
    text = models.TextField()
    likes = models.IntegerField(default=0)    
    
    datetime = models.DateTimeField(auto_now_add=True)
    
    def addLike(self):
        self.likes = self.likes + 1
        self.save()

    class Meta:
       ordering = ['-datetime']

    def __unicode__(self):
       return unicode(self.name)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class JokeLike(Like):
    joke = models.ForeignKey(Joke,on_delete=models.CASCADE)

# class CommentLike(Like):
#     comment =  models.ForeignKey(Comment,on_delete=models.CASCADE)