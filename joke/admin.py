from django.contrib import admin

 # Register your models here.
from .models import Joke,Comment
class CommentInline(admin.TabularInline):
    model = Comment
class JokeAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline
            ]
     
    list_display = ['id','joke','author','override','getCommentCount']
    pass
class CommentAdmin(admin.ModelAdmin):

    exclude = ['pic_id']


admin.site.register(Joke,JokeAdmin)
# admin.site.register(Comment,CommentAdmin)
