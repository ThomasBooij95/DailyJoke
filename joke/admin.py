from django.contrib import admin

 # Register your models here.
from .models import Joke,Comment

admin.site.register(Joke)
admin.site.register(Comment)
