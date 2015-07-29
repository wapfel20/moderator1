import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

    
  
class Comment(models.Model):
    text = models.TextField(max_length=150)
    timeDate = models.DateTimeField(auto_now=True)
    flagged = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s' % (self.text)
    
    class Meta:
      ordering = ['timeDate']
    
class MyRating(models.Model):
    postID = models.IntegerField()
    upVote = models.BooleanField(default=False)
    
    
class Post(models.Model):
    text = models.TextField(max_length=150)
    timeDate = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    flagged = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    anonymous = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return u'%s' % (self.text)
    
    class Meta:
      ordering = ['-rating','-timeDate']

    
class Forum(models.Model):
    title = models.CharField(max_length=65, blank=True, null=True)
    ownerID = models.IntegerField()
    description = models.CharField(max_length=140, blank=True, null=True)
    forumType = models.CharField(max_length=65)
    archived = models.BooleanField(default=False)
    spreadsheetLink = models.URLField(blank=True, null=True)
    timeDate = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10)
    codeNecessary = models.BooleanField(default=True)
    allowJoin = models.BooleanField(default=True)
    posts = models.ManyToManyField(Post, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.title, self.dateTime)
    
    class Meta:
      ordering = ['timeDate']


class ModUser(models.Model):
    user = models.ForeignKey(User)
    job = models.CharField(max_length=65, blank=True, null=True)
    forums = models.ManyToManyField(Forum, blank=True, null=True)
    posts = models.ManyToManyField(Post, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    myRatings = models.ManyToManyField(MyRating, blank=True, null=True)
    profilePic = models.URLField(max_length=200, blank=True, null=True)
    
    
    def __unicode__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.user.email)
    
    class Meta:
      ordering = ['user__last_name']

    
    
    
    