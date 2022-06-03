from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

class Question(models.Model):
    CATEGORIES = [
        ('CMPLN', 'Complaint'),
        ('FMLY', 'Family'),
        ('FRNDS', 'Friends'),
        ('HBBS', 'Hobbies'),
        ('LV', 'Love'),
        ('OTHR', 'Other'),
        ('SCHL', 'School'),
        ('SPRTS', 'Sports'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORIES) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

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
    date = models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    # likes = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.body[:20]
    
    @property
    def num_days_ago(self):
        today= timezone.now()
        return (today - self.date).days
    
    @property
    def num_likes(self):
        return self.like_set.count()

class PostComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment_text[:10]
    
    @property
    def num_days_ago(self):
        today= timezone.now()
        return (today - self.date).days



class Like(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    post_comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, null=True, blank=True)
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE, null=True, blank=True)