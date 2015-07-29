import json

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from google_login.models import GoogleUserInfo
from moderatorapp.models import Forum, Post, ModUser, Comment, MyRating


@login_required
def createForum(request):
    if request.method == 'POST':
        userInfo = ModUser.objects.get(user=request.user)
        forumTitle = request.POST['forumTitle'].strip().title()
        description = request.POST['description'].strip()
        forumType = request.POST['forumType'].strip()
        forumCode = generateCode()
        
        if Forum.objects.filter(title=forumTitle, ownerID=userInfo.id):
            return HttpResponse(json.dumps({'error':'Sorry, you already have a forum with that name.'}))
        else:
            myNewForum = Forum.objects.create(
                title = forumTitle,
                ownerID = userInfo.id,
                description = description,
                forumType = forumType,
                code = forumCode,
                
            )
            userInfo.forums.add(myNewForum)
            userInfo.save()
            
              
        
        data = {'forumID':myNewForum.id}
    else:
        data = {'error':"didn't work"}
                
    return HttpResponse(json.dumps(data))


@login_required
def createPost(request):
    if request.method == 'POST':
        userInfo = ModUser.objects.get(user=request.user)
        text = request.POST['post'].strip()
        forumID = request.POST['forumID'].strip()
        try:
            tryanonymous = request.POST['anonymous']
            anonymous = True
        except:
            anonymous = False
        
        
        myPost = Post.objects.create(
            text = text,
            rating = 0,
            anonymous = anonymous,
        )
            
        if GoogleUserInfo.objects.filter(user=request.user):
            googleUser = GoogleUserInfo.objects.get(user=request.user)
        else:
            googleUser = False
            
        userInfo.posts.add(myPost)
        userInfo.save()
        
        if Forum.objects.filter(id = forumID):
            myForum = Forum.objects.get(id = forumID)
            
            myForum.posts.add(myPost)
            myForum.save()
            
        else:
            args = {'error':"Oh boy... this is embarrassing. We can't seem to find your forum. So.... try again"}
        
        args = {
            'post':myPost,
            'userInfo':userInfo,
            'googleUser': googleUser,
            }
    else:
        args = {'error':"didn't work"}
                
    return render_to_response('post_display.html', args)




@login_required
def createComment(request):
    if request.method == 'POST':
        userInfo = ModUser.objects.get(user=request.user)
        text = request.POST['commentText'].strip()
        postID = request.POST['postID'].strip()
        
        
        if Post.objects.filter(id = postID):
            myPost = Post.objects.get(id = postID)
        
            myComment = Comment.objects.create(
                text = text,
            )
            
            userInfo.comments.add(myComment)
            userInfo.save()
        
            myPost.comments.add(myComment)
            myPost.save()
              
            
        else:
            args = {'error':"Oh boy... this is embarrassing. We can't seem to find your post. So.... try again"}
        
        args = {
            'currentComment':myComment,
            'userInfo':userInfo,
            }
    else:
        args = {'error':"didn't work"}
                
    return render_to_response('comment_display.html', args)


@login_required
def adjustRating(request):
    if request.method == 'POST':
        userInfo = ModUser.objects.get(user=request.user)
        rating = request.POST['rating'].strip()
        postID = request.POST['postID'].strip()
        
        bLetUserVote = True
        if MyRating.objects.filter(postID=postID, moduser=userInfo):
            myRating = MyRating.objects.get(postID=postID, moduser=userInfo)
            if rating == 'add' and myRating.upVote:
                bLetUserVote = False
                return HttpResponse(json.dumps({'error': "You have already voted on this one"}))
            elif rating == 'subtract' and myRating.upVote == False:
                bLetUserVote = False
                return HttpResponse(json.dumps({'error': "You have already voted on this one"}))
                
        
        if Post.objects.filter(id = postID) and bLetUserVote:
            ratedPost = Post.objects.get(id = postID)
            if rating == 'add':
                ratedPost.rating += 1
                upVote = True
            else:
                ratedPost.rating -= 1
                upVote = False
            ratedPost.save()
            
            if MyRating.objects.filter(postID=postID, moduser=userInfo):
                myRating = MyRating.objects.get(postID=postID, moduser=userInfo)
                myRating.upVote = upVote
            else:
                myRating = MyRating.objects.create(
                    postID = ratedPost.id,
                    upVote = upVote,
                )
            myRating.save()
            userInfo.myRatings.add(myRating)
            userInfo.save()
            
            args = {"success":"success"}
              
            
        else:
            args = {'error':"Oh boy... this is embarrassing. We can't seem to find this post. So.... try again"}
        
    else:
        args = {'error':"didn't work"}
                
    return HttpResponse(json.dumps(args))




#---------------------------------- Special Functions ----------------------------------------


import string
from time import time
from itertools import chain
from random import seed, choice, sample


def generateCode(length=5, digits=3, upper=0, lower=2):
    seed(time())

    lowercase = string.lowercase.translate(None, "o")
    uppercase = string.uppercase.translate(None, "O")
    letters = "{0:s}{1:s}".format(lowercase, uppercase)

    password = list(
        chain(
            (choice(uppercase) for _ in range(upper)),
            (choice(lowercase) for _ in range(lower)),
            (choice(string.digits) for _ in range(digits)),
            (choice(letters) for _ in range((length - digits - upper - lower)))
        )
    )

    return "".join(sample(password, len(password)))
