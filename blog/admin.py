from django.contrib import admin
from .models import Author, Post, Tag, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('title', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'comment', 'post')
    list_filter = ('username', 'comment')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)
