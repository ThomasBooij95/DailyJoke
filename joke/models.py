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

    
