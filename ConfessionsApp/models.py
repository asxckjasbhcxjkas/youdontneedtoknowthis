from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        text_len = len(self.question_text)
        if text_len > 20:
            return self.question_text[:20] + "...?"
        else:
            return self.question_text

    @property
    def num_days_ago(self):
        today= timezone.now()
        return (today - self.date).days

    @property
    def num_likes(self):
        return self.like_set.count()
    
    @property
    def num_posts(self):
        return self.post_set.count()

    @property
    def posts(self):
        return self.post_set.all()

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    edited = models.BooleanField(default=False)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        text_len = len(self.post_text)
        if text_len > 20:
            return self.post_text[:20] + "..."
        else:
            return self.post_text
    @property
    def num_days_ago(self):
        today= timezone.now()
        return (today - self.date).days

class Confession(models.Model):
    body = models.CharField(max_length=666)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    edited = models.BooleanField(default=False)
    edited_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.body[:20]
    
    @property
    def num_days_ago(self):
        today= timezone.now()
        return (today - self.date).days
    
    @property
    def num_likes(self):
        return self.like_set.count()

