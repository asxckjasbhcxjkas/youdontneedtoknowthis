from django.contrib import admin
from .models import (Question, Post, Confession)
# Register your models here.
admin.site.register(Question)
admin.site.register(Post)
admin.site.register(Confession)