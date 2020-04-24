from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Joke(models.Model):
    joke = models.TextField()
    # likes = models.IntegerField(default=0)
    # description = models.TextField(blank=True, null=True)
    
    # def addLike(self):
    #     self.likes = self.likes + 1
    #     self.save()
    def addJoke(self, jokeText):
        self.joke = jokeText
        self.save()



       
class Comment(models.Model):
    joke = models.ForeignKey(Joke,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pic_id = models.TextField()
    # likes = models.IntegerField(default=0)    
    
    datetime = models.DateTimeField(auto_now_add=True)
    
    #Not needed anymore just as in Joke, we can refer number of comment likes from the CommentLike class
    # def addLike(self):
    #     self.likes = self.likes + 1
    #     self.save()

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

    #Takes user object and joke object as input
    def userLikedJoke(current_user, current_joke):

        #Anonymous users CANNOT be used for the filter AND can also NOT like any comments
        if current_user.is_anonymous:
            return True

        userLikedJoke = JokeLike.objects.filter(user = current_user, joke = current_joke)
        # likedJokes = JokeLike.objects.get(user_id = user_id, joke_id = joke_id)
        if userLikedJoke:
            #did like the joke
            return True

        else:
            #Did NOT ike to joke (*empty array)
            return False