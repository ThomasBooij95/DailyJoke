from django.db import models
from django.urls import reverse

# Create your models here.


class Joke(models.Model):
    joke = models.TextField()
    # description = models.TextField(blank=True, null=True)
    