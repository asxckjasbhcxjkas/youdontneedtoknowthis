from django.contrib import admin
from .models import (Question, Post, 
                        PostComment, Like, Confession)
# Register your models here.
admin.site.register(Question)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Like)
admin.site.register(Confession)