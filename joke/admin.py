from django.contrib import admin

 # Register your models here.
from .models import Joke,Comment
class JokeAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    exclude = ['pic_id']


admin.site.register(Joke,JokeAdmin)
admin.site.register(Comment,CommentAdmin)
